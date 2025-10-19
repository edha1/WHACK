# InforMATE - WHACK

## Problem Statement (Brevan Howard Challenge)
Accurate information is critical for effective decision-making. However, distinguishing factual content from misleading or biased information is increasingly difficult.  
**Challenge:**  
> Build a solution that helps users understand and assess information accurately.

---

## Our Solution:

**InforMATE** is an **AI-powered Chrome extension** that helps users evaluate the accuracy of online information, from news headlines and tweets. The tool either extracts text from the active tab, or allows users to input text, and sends it to a Flask backend. It then leverages trained AI models to provide an accuracy score. It also supports **multilingual content** via Google Translate API, ensuring global applicability.

---

## Tech Stack:
**Extension:**
- Vanilla JavaScript  
- HTML/CSS  
- Chrome Extension APIs  

**Backend:**
- Python  
- Flask  
- 11 AI/ML Models (Custom-trained for content accuracy analysis)
---

## Setup Instructions:

1. Clone the repository. 

### Install requirements and start server:
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Running the chrome Extension
1. Open **chrome://extensions/** in your browser.  
2. Enable **Developer Mode**.  
3. Click **Load unpacked** and select the `extension/` folder.

---
## 🎬 Demo:

![Popup UI](demo/popup.png)

*Popup Ui*

![Accuracy Rating UI](demo/accuracy_rating.png)

*Displaying Accuracy Rating*

---
