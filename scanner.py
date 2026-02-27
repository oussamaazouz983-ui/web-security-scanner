import requests
from datetime import datetime

print("\n======================================")
print("     Web Security Scanner v1.0")
print("======================================")

url = input("Enter website URL (include http:// or https://): ")

risk_score = 0

try:
    print("\nScanning target...")
    response = requests.get(url, timeout=5)

    print("\n--- Basic Information ---")
    print("Scan Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Status Code:", response.status_code)

    # HTTPS Check
    if url.startswith("https"):
        print("HTTPS: Enabled ✅")
    else:
        print("HTTPS: Not Secure ❌")
        risk_score += 1

    # Security Headers
    print("\n--- Security Headers Check ---")

    security_headers = {
        "X-Frame-Options": "Protects against Clickjacking",
        "Content-Security-Policy": "Protects against XSS attacks",
        "Strict-Transport-Security": "Forces HTTPS usage",
        "X-Content-Type-Options": "Prevents MIME-type sniffing"
    }

    headers = response.headers

    for header, description in security_headers.items():
        if header in headers:
            print(f"{header}: Present ✅")
        else:
            print(f"{header}: Missing ❌ ({description})")
            risk_score += 1

    # Risk Evaluation
    print("\n--- Risk Evaluation ---")

    if risk_score == 0:
        print("Risk Level: LOW 🟢")
    elif risk_score <= 2:
        print("Risk Level: MEDIUM 🟡")
    else:
        print("Risk Level: HIGH 🔴")

except Exception as e:
    print("\nError connecting to website ❌")
    print("Error:", e)

print("\nScan Completed.")
print("======================================")