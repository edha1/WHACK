let btn = document.getElementById("get-input"); 
let header = ""; 
let date = ""; 
let content = ""; 

btn.addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tabId = tabs[0].id;

    chrome.scripting.executeScript({ target: { tabId }, files: ["content.js"] }, () => {
      
      // get title
      chrome.tabs.sendMessage(tabId, { action: "getH1" }, (response1) => {
        document.getElementById("header").innerText =
          response1?.h1?.join("\n") || "No <h1> found.";
      });

      // get date
      chrome.tabs.sendMessage(tabId, { action: "getDate" }, (response2) => {
        document.getElementById("date").innerText =
          response2?.date?.join("\n") || "No <time> found.";
      });

      // get content
      chrome.tabs.sendMessage(tabId, { action: "getContent" }, (response3) => {
        document.getElementById("content").innerText =
          response3?.content?.join("\n") || "No <p> found.";
      });

    });
  });
});

