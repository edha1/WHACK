chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getInformation") {


    // if looking at a twitter post, just send content to the model
    const tweetEl = document.querySelector('div[data-testid="tweetText"]');
    if (tweetEl) {
        const twitterData = tweetEl.innerText.trim();
        chrome.runtime.sendMessage(
        { action: "sendTwitterInfoToModel", twitterData },
        (response) => sendResponse(response)
        );
    } else {

    const articles = document.getElementsByTagName("article");
    const DATE_REGEX = /\b([1-9]|[12][0-9]|3[01])(st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\b/g;

    let header = "";
    let dates = [];
    let content = [];

    // get the header
    for (let article of articles) {
      const h1Elements = article.querySelectorAll("h1");
      header = Array.from(h1Elements).map((h1) => h1.innerText.trim());
    }

    // get the date 
    const dateFromTimeEl = document.getElementsByTagName("time");
    if (dateFromTimeEl.length > 0) {
      const datesUnfiltered = Array.from(dateFromTimeEl).map((d) => d.innerText.trim());
      dates = datesUnfiltered.filter((d) => DATE_REGEX.test(d));
    }

    // get the content
    for (let article of articles) {
      const allContent = article.querySelectorAll("p");
      content.push(...Array.from(allContent).map((p) => p.innerText.trim()));
    }

    // send to flask backend to input code into the model
    // TODO: make content not a list of paragraphs, and put title, new line, content
    chrome.runtime.sendMessage(
      { action: "sendNewsInfoToModel", header, content, date: dates },
      (response) => sendResponse(response)
    );
    }
    return true; 
  }

  
});