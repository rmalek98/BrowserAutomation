# Web Automation Script

This repository contains a Python script for automating interactions with a specific webpage using Selenium and pyautogui.

## Prerequisites

- Python 3.x
- Chrome WebDriver (chromedriver) - Ensure the correct path is set in the script.
- Required Python packages: `selenium`, `pyautogui`

## Installation

1. **Clone** this repository or **download** the script.

2. Set vertiual environment:
```bash
   python -m venv venv
```
3. Activate vertiual environment:
```bash
   source venv/bin/activate
```

3. Install the required Python packages:
```bash
   pip install selenium pyautogui
```

4. deactive vertiual environment:
```bash
   deactivate
```

Download and place the Chrome WebDriver (chromedriver) executable in the same directory as the script.
Customize the script:
Modify initial_window_x and initial_window_y with your desired browser window position.
Replace the URL in sign_in_url with the URL of the webpage you want to automate.
Adjust cursor coordinates and interactions in the automation section.
Usage

Run the script:
```bash
  taskAuto.py
```

The script will automate interactions with the specified webpage, including cursor movements, clicks, and text input.
Additional Information

The script utilizes Selenium for browser automation and pyautogui for simulating cursor interactions.
Make sure to install the necessary browser driver (chromedriver) compatible with your Chrome/Chromium version.
Disclaimer

This script is provided as-is and is meant for educational and personal use. Ensure you have the necessary permissions to automate interactions with websites.

## rmalek98
