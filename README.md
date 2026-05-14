# 🍪 Cookie Clicker Automation Bot

A robust Python-based automation script that interacts with the "Cookie Clicker" web game. This project demonstrates the application of **GUI automation**, **computer vision**, and **pixel-level color detection** to create an efficient "game bot."

---

## 🛠️ Technical Features

*   **Image Recognition:** Uses `PyAutoGUI` for template matching to identify the browser, cookie prompts, and language settings.
*   **Color-Logic Purchasing:** Scans specific UI regions for the "affordable" green color (`#66FF66`) to automate building upgrades.
*   **Event Handling:** Implements a global listener using the `keyboard` library for a safe, manual exit strategy.
*   **Object-Oriented Design:** The code is structured within a `Cookieclicker` class, making it modular and easy to maintain.

---

## 📂 Project Structure

```bash
├── main.py            # The core logic and bot class
├── browser.png        # Image used to locate the browser icon
├── webcookie.png      # Image used to locate web launch icon
├── english.png        # Image used for language selection
└── README.md          # Project documentation
```
---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.x** installed. You will also need to install the following dependencies:

```bash
pip install pyautogui keyboard Pillow
```
---

### 2. Configuration
The script is currently calibrated for specific screen coordinates. To adapt it to your monitor:

Update the self.buldings_regions list with your screen's specific coordinates.

Ensure your browser.png, webcookie.png, and english.png snippets are clear and reflect your desktop/browser theme.

---

### 3. Usage
Run the script through your terminal:

```Bash
python main.py
```
To Stop: Press the 'q' key at any time to terminate the bot safely.

---

## 🧪 Automation Logic (QA Perspective)
As a project focused on automation, several "edge cases" and stability measures were addressed:

State Management: The setup_game() method ensures the bot doesn't start clicking until the game is fully loaded and configured.

Wait Strategies: Uses time.sleep() and pyautogui.PAUSE to synchronize script execution with browser rendering speeds.

Error Handling: Utilizes try/except blocks to handle manual interrupts and prevent script crashes.
