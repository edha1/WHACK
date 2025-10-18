// send to the app.py to run into model
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "sendToModel") {
    fetch("http://localhost:5000/check-article", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        header: message.header,
        content: message.content,
        date: message.date,
      }),
    })
      .then((res) => res.json())
      .then((data) => sendResponse(data))
      .catch((err) => sendResponse({ error: err.message }));

    return true; // keep the message channel open
  }
});
