// Uso: node shoot.js PUERTO CARPETA_SALIDA [cuadros separados por coma] [query de split.html]
// Servir con: python3 -m http.server PUERTO (desde la carpeta que contiene r3d/ y los datos)
const { chromium } = require('playwright');
const [port, out, only, query] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('console', m => console.log('page:', m.text()));
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto(`http://127.0.0.1:${port}/r3d/split.html${query ? '?' + query : ''}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  const n = await p.evaluate('window.N');
  const list = only && only !== 'all' ? only.split(',').map(Number) : [...Array(n).keys()];
  for (const i of list) {
    await p.evaluate(i => window.setFrame(i), i);
    await p.locator('#stage').screenshot({ path: `${out}/${String(i).padStart(4, '0')}.png` });
  }
  await b.close();
  console.log('ok', list.length);
})();
