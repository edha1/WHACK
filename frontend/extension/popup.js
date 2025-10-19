let btn = document.getElementById("get-input"); 
let accuracy = document.getElementById("accuracy"); 
let headerEl = document.getElementById("header"); 
const pillEl   = document.getElementById('accuracy');
const cardEl   = document.getElementById('verdictCard');
const manInput = document.getElementById('manualInput'); 
let header = ""; 
let date = ""; 
let content = ""; 

btn.addEventListener("click", () => {
    const userText = manInput.value.trim();
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tabId = tabs[0].id;

    chrome.scripting.executeScript({ target: { tabId }, files: ["content.js"] }, () => {
        if (userText === "") { 
            chrome.tabs.sendMessage(tabId, { action: "getAccuracyFromPage" }, (response) => {
            if (chrome.runtime.lastError) {
                console.error("Error:", chrome.runtime.lastError.message);
                accuracy.innerHTML = "Error getting data.";
                return;
            }
            
            // change the text of the popup based on value of accuracy
            headerEl.textContent =
                output(response?.accuracy) || "Failed to see accuracy";
            });
        } else if (userText !== "") {
            chrome.tabs.sendMessage(tabId, { action: "getAccuracyFromInput", text: userText }, (response) => {
            if (chrome.runtime.lastError) {
                console.error("Error:", chrome.runtime.lastError.message);
                accuracy.innerHTML = "Error getting data.";
                return;
            }
            // change the text of the popup based on value of accuracy
            headerEl.textContent =
                output(response?.accuracy) || "Failed to see accuracy";
            });
        }
    });
  });
});

const output = (label) => {
  const rounded = (label * 100).toFixed(0);

  cardEl.style.borderColor = 'var(--border)';
  pillEl.style.background = 'var(--pill)';

  if (label >= 0.75) {
    accuracy.textContent = `${rounded}/100`;
    pillEl.style.background = 'var(--good)';
    cardEl.style.borderColor = 'var(--good)';
    return 'Highly likely to be real';
  }

  if (label >= 0.5) {
    accuracy.textContent = `${rounded}/100`;
    pillEl.style.background = 'var(--warn)';
    cardEl.style.borderColor = 'var(--warn)';
    return 'Likely to be real';
  }

  if (label >= 0.25) {
    accuracy.textContent = `${rounded}/100`;
    pillEl.style.background = 'var(--warn)';
    cardEl.style.borderColor = 'var(--warn)';
    return 'Possibly fake';
  }

  accuracy.textContent = `${rounded}/100`;
  pillEl.style.background = 'var(--bad)';
  cardEl.style.borderColor = 'var(--bad)';
  return 'Quite possibly fake';
};
