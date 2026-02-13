# API Health Monitor (Python CLI Tool)

## Overview
API Health Monitor is a Python-based command-line tool that checks the availability and response time of multiple APIs.  
It is designed to simulate real-world cloud monitoring and automation tasks commonly performed by Cloud Engineers.

## Features
- Reads API endpoints from a configuration file
- Sends HTTP requests to each endpoint
- Reports status (UP/DOWN) and response time
- Logs results with timestamps
- Designed to run locally or on a cloud server (EC2)

## Tech Stack
- Python 3
- requests
- JSON configuration
- CLI execution
- Virtual environments (venv)

## Project Structure
api-health-monitor/
├── venv/
├── main.py
├── monitor.py
├── utils.py
├── config.json
├── results.log
├── requirements.txt
└── README.md