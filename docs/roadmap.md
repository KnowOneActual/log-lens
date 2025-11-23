# 🗺️ Project Roadmap

This document outlines the development plan for **Log Lens**. The goals are grouped by version milestones, focusing on moving from a basic CLI tool to a comprehensive log analysis suite.


## ✅ Completed (v1.0.0)



* [x] **Core Parsing Engine**: Basic regex-based log parsing.
* [x] **Log Level Detection**: Auto-counts INFO, WARN, ERROR, etc.
* [x] **IP Tracking**: Extracts and ranks IPv4 addresses.
* [x] **JSON Export**: Ability to save analysis data to report.json.
* [x] **CLI Interface**: Robust command-line arguments using argparse.
* [x] **Unit Tests**: Basic test suite for the parser logic.


## 🚧 Phase 2: Visualization & Reporting (Target: v1.1.0)

*Focus: Making the data easier for humans to read.*



* [ ] **HTML Reports**: Generate a standalone .html file with charts (using Plotly or Chart.js) to visualize error rates over time.
* [ ] **Time-Based Analysis**: Parse timestamps to detect "spikes" in errors (e.g., "500 errors per minute").
* [ ] **CSV Export**: Add support for exporting data to CSV for easy opening in Excel.


## 🚀 Phase 3: Performance & Intelligence (Target: v1.2.0)

*Focus: Handling massive files and smarter filtering.*



* [ ] **Streaming Read**: Optimize file reading to handle multi-gigabyte log files without consuming RAM.
* [ ] **Custom Regex**: Allow users to pass their own regex patterns via a config file (e.g., config.yaml).
* [ ] **Filtering**: Add CLI flags to filter output (e.g., --only-errors or --exclude-ip 127.0.0.1).


## 📦 Phase 4: Distribution (Target: v2.0.0)

*Focus: Making the tool shareable and installable.*



* [ ] **PyPI Package**: Structure the project to be installable via pip install log-lens.
* [ ] **Docker Support**: Create a Dockerfile to run the analyzer in a containerized environment.
* [ ] **CI/CD**: Update GitHub Actions to automatically run tests on every Pull Request.


## 💡 Future Concepts (Brainstorming)



* **Live Monitoring**: A "tail" mode that watches a log file in real-time (like tail -f).
* **GeoIP Lookup**: Convert IP addresses into geographic locations (Country/City).
* **Slack/Discord Alerts**: Send a message to a webhook if a specific error threshold is crossed.