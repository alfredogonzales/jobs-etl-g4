from prefect import task
import requests
from bs4 import BeautifulSoup

@task
def extract_cars():
    print("EXTRACCIÓN DE OFERTAS DE CARROS SEMINUEVOS")
    # URL de ejemplo, reemplazar con la URL real de la página de ofertas de carros seminuevos
    url = "https://neoauto.com/venta-de-autos-seminuevos"  # Reemplaza por URL real
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    car_options = soup.select("")
    print(f"Se encontraron {len(car_options)} carros seminuevos.")

    cars = []
    for car_option in car_options:
        title_tag = car_option.select_one("")
        price_tag = car_option.select_one("")
        mileage_tag = car_option.select_one("")
        location_tag = car_option.select_one("")
        fuel_tag = car_option.select_one("")
        transmission_tag = car_option.select_one("")
        link_tag = car_option.select_one("")
        date_tag = car_option.select_one("")

        car = {
            "titulo": title_tag.text.strip() if title_tag else None,
            "precio": price_tag.text.strip() if price_tag else None,
            "kilometraje": mileage_tag.text.strip() if mileage_tag else None,
            "ubicacion": location_tag.text.strip() if location_tag else None,
            "combustible": fuel_tag.text.strip() if fuel_tag else None,
            "transmision": transmission_tag.text.strip() if transmission_tag else None,
            "enlace": link_tag["href"].strip() if link_tag else None,
            "fecha": date_tag["datetime"] if date_tag and date_tag.has_attr("datetime") else None
        }

        cars.append(car)

    return jobs