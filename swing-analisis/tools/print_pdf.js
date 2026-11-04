// Imprime un HTML a PDF A4. Uso: node print_pdf.js URL SALIDA.pdf
const { chromium } = require('playwright');
const [url, out] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close(); console.log('ok', out);
})();
