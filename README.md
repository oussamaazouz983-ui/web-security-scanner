\# 🔐 Web Security Scanner v1.0



A beginner-friendly Python-based web security scanner that analyzes basic security configurations of a website.



---



\## 📌 Project Overview



This tool scans a website and evaluates its basic security posture by checking:



\- Website reachability  

\- HTTPS usage  

\- Presence of important security headers  

\- Overall risk level (Low / Medium / High)  



The goal of this project is to practice cybersecurity fundamentals and automation using Python.



---



\## 🛠 Technologies Used



\- Python 3  

\- requests library  

\- datetime module  



---



\## 🧠 Security Headers Checked



| Header | Purpose |

|--------|---------|

| X-Frame-Options | Protects against Clickjacking |

| Content-Security-Policy | Protects against Cross-Site Scripting (XSS) |

| Strict-Transport-Security | Forces HTTPS usage |

| X-Content-Type-Options | Prevents MIME-type sniffing |



---



\## ▶️ How to Run



\### 1️⃣ Install dependencies



```bash

pip install requests



2️⃣ Run the scanner



python scanner.py



3️⃣ Enter a target website when prompted



Example:



(https://google.com)



📊 Example Output





======================================

&nbsp;       Web Security Scanner v1.0

======================================



Scanning target...



--- Basic Information ---

Status Code: 200

HTTPS: Enabled ✅



--- Security Headers Check ---

X-Frame-Options: Present ✅

Content-Security-Policy: Missing ❌

Strict-Transport-Security: Missing ❌

X-Content-Type-Options: Missing ❌



--- Risk Evaluation ---

Risk Level: HIGH 🔴

======================================

