// send message to content.js so it can interact with the webpage
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    let h1Texts = ""; 
    let dates = ""; 
    let content = []; 
    const articles = document.getElementsByTagName("article"); 
    const DATE_REGEX = /\b([1-9]|[12][0-9]|3[01])(st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\b/g;

    // getting the title of the data
    if (message.action === "getH1") {
        for (let article of articles) {
            const h1Elements = article.querySelectorAll("h1");
            h1Texts = Array.from(h1Elements).map(h1 => h1.innerText.trim());
        }

    // get the date of the data
    } else if (message.action === "getDate") {
        const dateFromTimeEl = document.getElementsByTagName("time"); // date might not be under the time tag for all websites 
        let datesUnfiltered = ""; 
        if (dateFromTimeEl.length > 0) {
            datesUnfiltered = Array.from(dateFromTimeEl).map(date => date.innerText.trim()); 
            dates = datesUnfiltered.filter(date => DATE_REGEX.test(date));
        }
    } else if (message.action === "getContent") { 
        for (let article of articles) {
            const allContent = article.querySelectorAll("p");
            content.push(...Array.from(allContent).map(p => p.innerText.trim()));
        }
    }

    sendResponse({ h1: h1Texts, date: dates, content: content});
});