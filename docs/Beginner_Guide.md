# NopeRi: Developer Guide
## What It Does
NopeRi is a lightweight Python API client for Naukri.com, allowing users to interact with the Naukri job search application. It provides a simple way to search and apply for jobs on the platform.

## How It Works
* The `main.py` script serves as the entry point, utilizing the `NaukriJobClient` class from `src/client/job_client.py` to search and interact with job listings.
* The `NaukriLoginClient` class from `src/client/naukri_client.py` handles Naukri login sessions, while the `build_session` function from `src/client/session.py` creates an HTTP session.
* The `JobFilterPipeline2` class from `src/client/jop_classifier.py` filters job listings based on specific criteria.
* The client also uses various utility functions, such as those in `src/utils/extractors.py` and `src/utils/nkparam_generator.py`, to extract form keys and generate naukri parameters.

## Key Files
| File | Read this when... |
|------|------------------|
| `main.py` | You want to understand the application's entry point. |
| `src/client/job_client.py` | You need to interact with job listings. |
| `src/utils/dbhandler.py` | You want to store or retrieve naukri parameters from the database. |

## Start Here
To begin reading the code, start with the `main.py` script, which provides a clear overview of the application's flow. From there, you can explore the various modules and classes, such as `NaukriJobClient` and `NaukriLoginClient`, to gain a deeper understanding of the client's functionality. The `README.md` file also provides a brief introduction to the project and its purpose.