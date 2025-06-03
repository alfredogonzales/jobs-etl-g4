from prefect import task
import mysql.connector

@task
def load_cars(cars):
    print("CARGA DE OFERTAS DE CARROS SEMINUEVOS")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_g4"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autos_seminuevos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255),
            precio DOUBLE,
            kilometraje VARCHAR(50),
            ubicacion VARCHAR(255),
            combustible VARCHAR(50),
            transmision VARCHAR(50),
            enlace LONGTEXT
        )
    """)

    for car in cars:
        cursor.execute("""
            INSERT INTO autos_seminuevos (titulo, precio,kilometraje,ubicacion,combustible,transmision,enlace)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (car["titulo"], car["precio"], car["kilometraje"], car["ubicacion"], car["combustible"], car["transmision"], car["enlace"]))

    conn.commit()
    cursor.close()
    conn.close()