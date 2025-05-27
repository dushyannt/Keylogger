# System Monitoring Tool

## Overview
This project is a Python-based system monitoring tool that performs the following tasks:
- Records keystrokes and stores them in a text file.
- Retrieves computer information and stores it in an Excel file.
- Captures clipboard information and stores it in a text file.
- Retrieves Google Chrome browsing history and stores it in an Excel file.
- Takes a screenshot of the computer screen and saves it as a PNG file.

## Author
- **Dushyant Vashishtha**

## Prerequisites
- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - pynput
  - pandas
  - Pillow
  - pywin32
  - requests
  - openpyxl

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure Google Chrome is closed before running the script.
2. Run the script:
   ```bash
   python Spyware_tool.py
   ```
3. The script will perform the following actions:
   - Record keystrokes (press `ESC` to stop).
   - Save system information to `keystrokes.xlsx`.
   - Save clipboard contents to `clipboard.txt`.
   - Save Chrome browsing history to `search_history.xlsx`.
   - Take a screenshot and save it as `screenshot.png`.

## Output Files
- `logs.txt`: Contains recorded keystrokes.
- `keystrokes.xlsx`: Contains system information.
- `clipboard.txt`: Contains clipboard contents.
- `search_history.xlsx`: Contains Chrome browsing history.
- `screenshot.png`: Contains the screenshot.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Thanks to all contributors and supporters of this project.

# Spyware

Hey you all this is Ashutosh Behera. I have developed this advanced spyware tool to demonstrate the working of the spyware and how it tries to steal user's data.

DISCLAMIER

This python program is for educational purpose only. Don't use it for any malicious purpose. The authoe of this program will not be responsible for any kind of malicious activity.

WHAT IS A SPYWARE

Spyware is a type of malicious software -- or malware -- that is installed on a computing device without the end user's knowledge. It invades the device, steals sensitive information and internet usage data, and relays it to advertisers, data firms or external users.

WHAT ARE THE FEATURES OF THIS CODE

(1)Record keystrokes and store it in a text file.

(2)Record clipboard in a text file.

(3)Record google search history and store in an excel file.

(4)Retrieve user system's information like IP address, host, OS etc.

(5)Finally take a screenshot when you stop the program.

