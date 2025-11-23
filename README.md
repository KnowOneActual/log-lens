# Log Lens 🔍

 # **Under Develoment** 

**Log Lens** is a lightweight, robust command-line tool for analyzing server log files. It parses raw log data to extract key metrics, identify error patterns, and track IP address activity.

## 🚀 Features

* **Dynamic Log Level Detection**: Automatically counts `INFO`, `WARN`, `ERROR`, and `DEBUG` entries.
* **IP Address Tracking**: Identifies and ranks the top IP addresses hitting your server.
* **JSON Export**: Generate structured reports for external processing.
* **Resilient Parsing**: Handles large files and ignores binary garbage without crashing.

## 🛠 Installation

Clone the repository:

```bash
git clone [https://github.com/YOUR_USERNAME/log-lens.git](https://github.com/YOUR_USERNAME/log-lens.git)
cd log-lens
````

## 📖 Usage

**Basic Analysis (Console Output):**

```bash
python3 -m log_lens.main access.log
```

**Export to JSON:**

```bash
python3 -m log_lens.main access.log --export report.json
```

## 🧪 Running Tests

This project includes a unit test suite.

```bash
python3 -m unittest discover tests
```

