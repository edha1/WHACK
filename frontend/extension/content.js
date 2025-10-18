
// send message to content.js so it can interact with the webpage
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "getH1") {
        const h1Elements = document.getElementsByTagName("h1");
        const h1Texts = Array.from(h1Elements).map(h1 => h1.innerText.trim());
        sendResponse({ h1s: h1Texts });
    }
});
