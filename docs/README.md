# NopeRi
## Overview
NopeRi is a lightweight, Selenium-free Python API client for Naukri, designed to interact with the Naukri job search API. It provides a range of features, including job searching, user login, and session management, making it a useful tool for automating job searches and applications.

## Key Modules
| File | Purpose |
|------|---------|
| `main.py` | Main entry point of the application, responsible for searching for jobs on Naukri |
| `src/client/naukri_client.py` | Handles user login to Naukri, establishing a session and caching user data |
| `src/utils/dbhandler.py` | Provides a class for handling a SQLite database containing Naukri parameters |
| `src/utils/request_helper.py` | Offers a decorator with exponential-backoff retry logic for network/IO operations |

## Usage
To get started with NopeRi, you can use the `main.py` module as an example. For instance, you can use the `naukri_client` module to establish a session and search for jobs:
```python
from src.client.naukri_client import NaukriClient

client = NaukriClient()
client.login()
client.search_jobs()
```