chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getInformation") {

    
    const pageLang = document.documentElement.lang || "unknown";
    // if looking at a twitter post, just send content to the model
    const tweetEl = document.querySelector('div[data-testid="tweetText"]');
    if (tweetEl) {
        const twitterData = " " + "\n" + tweetEl.innerText.trim();
        chrome.runtime.sendMessage(
        { action: "sendTwitterInfoToModel", twitterData },
        (response) => sendResponse(response)
        );
    } else {

    const articles = document.getElementsByTagName("article");

    let header = "";
    let paragraphArr = [];

    // get the header of the article
    for (let article of articles) {
      const h1Elements = article.querySelectorAll("h1");
        if (h1Elements.length > 0) {
          header = h1Elements[0].innerText.trim(); 
          break; // only need first one
        }
    }

    // get the content of article 
    for (let article of articles) {
        const allContent = article.querySelectorAll("p");
        paragraphArr.push(
          ...Array.from(allContent)
            .map((p) => p.innerText.trim())
            .filter((text) => text.length > 0)
        );
      }

    // join all paragraphs into one continuous string
    const content = paragraphArr.join(" "); 
    // combine header + newline + content to match model input 
    const newsData = header + "\n" + content; 
    

    chrome.runtime.sendMessage(
      { action: "sendNewsInfoToModel", newsData: newsData, language: pageLang },
      (response) => sendResponse(response)
    );
    }
    return true; 
  }

  
});