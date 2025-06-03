from prefect import task
from datetime import datetime

@task
def transform_cars(cars):
    print("TRANSFORMACIÓN DE OFERTAS DE CARROS SEMINUEVOS")
    for car in cars:
        try:
            if car["date"] is not None:
                car["date"] = datetime.strptime(car["date"], "%d %b %Y").date()
        except ValueError:
            car["date"] = None
    return cars