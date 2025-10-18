// send to the app.py to run into model
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    // if news article 
  if (message.action === "sendNewsInfoToModel") {
    fetch("http://localhost:5000/check-article", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        newsData: message.newsData,
        language: message.language
      }),
    })
      .then((res) => res.json())
      .then((data) => sendResponse(data))
      .catch((err) => sendResponse({ error: err.message }));

    return true; // keep the message channel open

    // if twitter post 
  } else if (message.action === "sendTwitterInfoToModel") {
    fetch("http://localhost:5000/check-article", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        twitterData: message.twitterData
      }),
    })
      .then((res) => res.json())
      .then((data) => sendResponse(data))
      .catch((err) => sendResponse({ error: err.message }));
  }
});
