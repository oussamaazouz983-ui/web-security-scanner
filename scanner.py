import requests
import socket
from datetime import datetime


def scan_ports(host):
    print("\n--- Port Scan ---")

    common_ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL"
    }

    for port, service in common_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"Port {port} ({service}): OPEN ✅")
            else:
                print(f"Port {port} ({service}): Closed ❌")

            sock.close()

        except Exception as e:
            print(f"Error scanning port {port}: {e}")


print("\n======================================")
print("     Web Security Scanner v2.0")
print("======================================")

url = input("Enter website URL (include http:// or https://): ")

risk_score = 0

try:
    print("\nScanning target...")
    response = requests.get(url, timeout=5)

    host = url.replace("https://", "").replace("http://", "").split("/")[0]
    scan_ports(host)

    print("\n--- Basic Information ---")
    print("Scan Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Status Code:", response.status_code)

    if url.startswith("https"):
        print("HTTPS: Enabled ✅")
    else:
        print("HTTPS: Not Secure ❌")
        risk_score += 1

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