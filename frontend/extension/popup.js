let btn = document.getElementById("get-input"); 
    btn.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tabId = tabs[0].id; // get current tab 
    
    // inject content.js 
    chrome.scripting.executeScript({ target: { tabId }, files: ["content.js"] }, () => {
        chrome.tabs.sendMessage(tabId, { action: "getH1" }, (response) => {
        console.log(response);

        // test title text 
        document.getElementById("output").innerText = response?.h1s?.join("\n") || "No <h1> found.";
        });
    });
    });

});
