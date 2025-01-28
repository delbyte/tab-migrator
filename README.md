# Browser Tab Migrator

A Python tool for migrating open browser tabs from one browser to another. This project is a work in progress and aims to simplify the process of copying tab URLs from one browser and storing them for use in another browser.

---

## Features (Planned)

- Detect the number of open tabs in the current browser.
- Copy the URLs of all open tabs.
- Store the copied URLs in a text file for easy migration.
- Automate the opening of stored URLs in a different browser (coming soon).

---

## How It Works

The script uses the following steps:

1. **Tab Detection**: Identifies the number of tabs open in the current browser window.
2. **URL Extraction**: Iterates through the open tabs, copies their URLs, and appends them to a list.
3. **Storage**: Saves the URLs to a `migrator.txt` file for migration purposes.

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required dependencies:
   ```bash
   pip install pyautogui pyperclip
   ```

---

## Usage

1. Run the script and switch to the browser you want to migrate tabs from:
   ```bash
   python tab_migrator.py
   ```
2. The script will automatically:
   - Detect the number of open tabs.
   - Copy each tab's URL.
   - Save the URLs to a `migrator.txt` file.

---

## Dependencies

- **pyautogui**: For simulating keyboard and mouse actions.
- **pyperclip**: For clipboard operations.
- **time**: For delays between automated actions.

Install dependencies using:

```bash
pip install pyautogui pyperclip
```

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions.

