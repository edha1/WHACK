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

/* ===== InforMATE Add-on: confidence → UI ===== */

// Band from probability p in [0,1]
function informateBandFromConfidence(p) {
  if (p >= 0.75) return 'good';      // most likely real
  if (p >= 0.50) return 'warn';      // uncertain — leans real
  if (p >= 0.25) return 'warn';      // uncertain — leans fake
  return 'bad';                      // most likely fake
}

// Headline text per band (uses p to disambiguate warn)
function informateTextFromConfidence(p, band) {
  if (band === 'good') return 'This post is most likely real';
  if (band === 'bad')  return 'This post is most likely fake';
  return (p >= 0.50) ? 'Uncertain — leans real' : 'Uncertain — leans fake';
}

// Main renderer (safe to call from your existing flow)
// Accepts either { p: 0..1 } or { score: 0..100 }. Optional: { agree, total }.
function informateRenderFromConfidence(opts) {
  const headerEl = document.getElementById('header');
  const pillEl   = document.getElementById('accuracy');
  const cardEl   = document.getElementById('verdictCard');

  const hasScore = typeof opts.score === 'number';
  const hasP     = typeof opts.p === 'number';
  const p        = hasP ? Math.max(0, Math.min(1, opts.p))
                        : hasScore ? Math.max(0, Math.min(100, opts.score)) / 100
                                   : 0.5;

  const band     = informateBandFromConfidence(p);
  const text     = informateTextFromConfidence(p, band);
  const score100 = Math.round(p * 100);

  cardEl.classList.remove('good','warn','bad');
  cardEl.classList.add(band);

  headerEl.textContent = text;
  pillEl.textContent   = `${score100}/100`;

  // If you later want to show agreement in the subline:
  // const sub = document.getElementById('content');
  // if (opts.total && typeof opts.agree === 'number') {
  //   sub.textContent = `${opts.agree}/${opts.total} models agree`;
  // }
}

/* ===== End Add-on ===== */