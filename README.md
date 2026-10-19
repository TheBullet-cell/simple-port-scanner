# Simple Port Scanner

A beginner-friendly Python script that scans common ports on a target IP address.

## 📌 Description

This is a simple port scanner built with Python's built-in `socket` library. It checks whether common ports (like HTTP, HTTPS, SSH, FTP, etc.) are open or closed on a target machine.

This project was built as part of my journey to learn Python and cybersecurity fundamentals.

## 🚀 Features

- Scans a predefined list of common ports.
- Uses TCP connection (`SOCK_STREAM`).
- Includes a 1-second timeout per port to avoid hanging.
- Simple and clean output.

## ⚙️ Requirements

- Python 3.x
- No external libraries required (only `socket`, which is built-in).

## 🛠️ How to Run

1. Clone this repository or download the script.
2. Open a terminal in the project folder.
3. Run the script: `python port_scanner.py`
4. Enter a target IP address (e.g., `127.0.0.1` for localhost).
5. Wait for the scan to finish. The results will be printed in the terminal.

## 🧠 How It Works

The script defines a function `scan_port(ip, port)` that creates a TCP socket and attempts to connect to the given IP and port. It returns `True` if the port is open (`result == 0`) and `False` otherwise. It then loops through a list of common ports and prints their status.

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Do not use it to scan networks or devices you do not own or have explicit permission to test. Unauthorized scanning is illegal and unethical.

## 👤 Author

- GitHub: [TheBullet-cell](https://github.com/TheBullet-cell)
- YouTube: [ZeroBullet Tech](https://www.youtube.com/@ZeroBulletTech)

## 📜 License

This project is open-source and available under the MIT License.
