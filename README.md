# 🔍 LoopFuzz

LoopFuzz is a lightweight **Python-based fuzzing tool** designed to discover hidden directories and paths in web applications.  
Inspired by classic security tools, LoopFuzz aims to be simple, fast, and effective. 🚀

---

## ✨ Features

- 📂 **Wordlist support**: use custom wordlists to brute-force directories.  
- 🌐 **HTTP requests**: performs GET requests and reports status codes.  
- 🎯 **Available modes**:  
  - `BFUZZ` → basic directory fuzzing.  
  - `DFUZZ` → (under development).  
- 🛑 **Ignore status codes**: skip unwanted responses (e.g., 404).  
- 📊 **Summary report**: shows how many requests were made once the wordlist is completed.  

---

## ⚙️ Installation

Clone the repository and make sure you have Python 3 installed:

```bash
git clone https://github.com/marcos-ux90/LoopFuzz.git
cd LoopFuzz
pip install -r requirements.txt
python3 setup.py --help
