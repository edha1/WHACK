let btn = document.getElementById("get-input"); 
let accuracy = document.getElementById("accuracy"); 
let header = ""; 
let date = ""; 
let content = ""; 

btn.addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tabId = tabs[0].id;

    chrome.scripting.executeScript({ target: { tabId }, files: ["content.js"] }, () => {

        chrome.tabs.sendMessage(tabId, { action: "getInformation" }, (response) => {
            if (chrome.runtime.lastError) {
                console.error("Error:", chrome.runtime.lastError.message);
                accuracy.innerHTML = "Error getting data.";
                return;
            }
            
            // for testing, see the title, content and date 
            document.getElementById("content").innerText =
                response?.received.content?.join("\n") || "No <p> found.";

            document.getElementById("header").innerText =
                response?.received.header?.join("\n") || "No <h1> found.";

            document.getElementById("date").innerText =
                response?.received.date?.join("\n") || "No <time> found.";

            // TODO: need to add to output the responses
            // output(response?.received.);
        });

    });
  });
});

// TODO: change for percentage output 
const output = (label) => {
    if (label == "1") {
        accuracy.innerHTML = "Likely to be accurate"; 
    } else if (label == "0") {
        accuracy.innerHTML = "Unlikely to be accurate"; 
    }
}

