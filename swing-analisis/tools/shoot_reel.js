// Saca los cuadros del reel compuesto. Uso: node shoot_reel.js PUERTO PAGINA CARPETA DESDE HASTA
const { chromium } = require('playwright');
const [port, page, out, from, to] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto(`http://127.0.0.1:${port}${page}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  const el = p.locator('#stage');
  for (let k = +from; k < +to; k++) {
    await p.evaluate(k => window.setFrame(k), k);
    await el.screenshot({ path: `${out}/${String(k).padStart(5, '0')}.png` });
  }
  await b.close(); console.log('ok', from, to);
})();
