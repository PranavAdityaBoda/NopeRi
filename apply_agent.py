def fetch_all_jobs(jc: NaukriJobClient) -> list:
    # ... existing code ...

    all_jobs = []
    for query in BQUERIES:
        jobs = jc.search_jobs(keyword=query["keyword"], location=query["location"], experience=EXPERIENCE_LEVELS[0])
        for job in jobs:
            if job.company.lower() != "google" and job.company.lower() not in ["google llc", "google india", "google inc."]:
                all_jobs.append(job)
            else:
                print(f"Skipping job from Google: {job.title}")

    return all_jobs