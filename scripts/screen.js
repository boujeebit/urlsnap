try {
  if (process.argv[2]) {
    const puppeteer = require('puppeteer');
    (async () => {
      try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.setViewport({width:1366,height:768});
        // How long do I want to wait?
        await page.setDefaultNavigationTimeout(10000);

        // 'Protocol error (Page.navigate): Cannot navigate to invalid URL undefined'
        // https://github.com/GoogleChrome/puppeteer/issues/1390
        try {
          await page.goto(process.argv[2]);
        } catch (error) {
          console.log('3');
          browser.close();
          process.exit(0);
        }
        
        await page.screenshot({path: './images/'+process.argv[3], fullPage: true});
        await browser.close();
        console.log('0');
      } catch (error) {
        console.log('2');
        await browser.close();
        process.exit(0);
      }
    })();
  }
} catch (error) {
  console.log('1');
  process.exit(0);
}


