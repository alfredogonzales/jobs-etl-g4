##from prefect import task

##@task
##def transform_jobs():
##    print("TRANSFORMACIÓN DE OFERTAS DE LINKEDIN")

from prefect import task
from datetime import datetime

@task
def transform_jobs(jobs):
    print("TRANSFORMACIÓN DE OFERTAS DE LINKEDIN")
    for job in jobs:
        try:
            if job["date"] is not None:
                job["date"] = datetime.strptime(job["date"], "%d %b %Y").date()
        except ValueError:
            job["date"] = None
    return jobs