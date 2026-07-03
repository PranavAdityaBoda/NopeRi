# NopeRi API Reference
## Modules
### `main.py`
Serves as the main entry point for the Naukri job search application. Key functions/classes:
* `load_applied_jobs`, loads set of job IDs already applied
* Handles loading of the application

### `src/client/job_client.py`
Provides a `NaukriJobClient` class for searching and retrieving job listings. Key functions/classes:
* `NaukriJobClient`, searches and retrieves job listings from Naukri
* Handles job listing retrieval

### `src/client/naukri_client.py`
Offers a `NaukriLoginClient` class for authenticating and managing Naukri sessions. Key functions/classes:
* `NaukriLoginClient`, handles login and session management
* Authenticates with Naukri services

### `src/utils/dbhandler.py`
Provides a SQLite database handler for storing Naukri parameters. Key functions/classes:
* `dbhandler`, handles database operations for Naukri parameters
* Stores and retrieves Naukri parameters

### `src/utils/nkparam_generator.py`
Generates a Naukri parameter token based on the provided page type. Key functions/classes:
* `nkparam_generator`, generates Naukri parameter tokens
* Handles Naukri parameter generation

## Quick Reference
| Symbol | Description |
|--------|-------------|
| `NaukriLoginClient` | Handles login and session management |
| `NaukriJobClient` | Searches and retrieves job listings |
| `load_applied_jobs` | Loads set of job IDs already applied |
| `nkparam_generator` | Generates Naukri parameter tokens |
| `dbhandler` | Handles database operations for Naukri parameters |