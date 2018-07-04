if (process.argv[2]) {
  const puppeteer = require('puppeteer');
  console.log(process.argv[3]);
  (async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const override = Object.assign(page.viewport(), {width: 1366});
    await page.setViewport(override);
    await page.goto(process.argv[2]);
    await page.screenshot({path: './images/'+process.argv[3], fullPage: true});
    await browser.close();
  })();
}