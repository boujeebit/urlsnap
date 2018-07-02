if (process.argv[2]) {
  const puppeteer = require('puppeteer');

  (async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const override = Object.assign(page.viewport(), {width: 1366});
    await page.setViewport(override);
    await page.goto(process.argv[2]);
    await page.screenshot({path: './images/example.png', fullPage: true});
    await browser.close();
  })();
}