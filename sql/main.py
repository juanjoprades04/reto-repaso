import os, psycopg
from datetime import datetime, timezone

url = os.getenv("DATABASE_URL")

try:
    connection = psycopg.connect(url)
    cur = connection.cursor()
    print("BD conectada con éxito")
except Exception as e:
    print("Error conectando a la BD:", e)
    exit()

now = datetime.now(timezone.utc)

personajes = [
    ("Azulejo Prime",     "Alive",   "Robot", "Glazing unit",   "Genderless", "Castellón Kiln-7",     "Planta de esmaltado", None, None, now),
    ("Terracota Ruiz",    "Alive",   "Human", "",               "Female",     "Onda",                 "Taller de prensado",  None, None, now),
    ("Gres el Vigilante", "Alive",   "Robot", "Security bot",   "Male",       "Castellón Kiln-7",     "Almacén central",     None, None, now),
    ("Zorblax Mosaico",   "unknown", "Alien", "Silicate being", "unknown",    "Nebulosa Caolín",      "Horno túnel",         None, None, now),
    ("Porcelana Vidal",   "Alive",   "Human", "",               "Female",     "Vila-real",            "Laboratorio de I+D",  None, None, now),
    ("Klinker-9",         "Dead",    "Robot", "Kiln drone",     "Genderless", "Castellón Kiln-7",     "Desguace",            None, None, now),
    ("Mayólica Brenn",    "Alive",   "Alien", "Shapeshifter",   "Female",     "Nebulosa Caolín",      "Showroom",            None, None, now),
    ("Jaume Engobe",      "Alive",   "Human", "",               "Male",       "L'Alcora",             "Planta de esmaltado", None, None, now),
    ("Esmalte Qor",       "unknown", "Alien", "Crystal mind",   "unknown",    "Anillo de Feldespato", "Horno túnel",         None, None, now),
    ("Rakú la Errante",   "Dead",    "Ghost", "Kiln spirit",    "Female",     "Horno anagama",        "Desconocida",         None, None, now),
]

query = """
    INSERT INTO characters
        (name, status, species, type, gender, origin_name,
         location_name, image, url)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
"""
cur.executemany(query, personajes)
connection.commit()
print("Personajes insertados")


query = "SELECT id, name, species FROM characters ORDER BY id LIMIT 10;"
cur.execute(query)

filas = cur.fetchall()

for fila in filas:
    print(fila[0], fila[1], fila[2])


cur.execute("SELECT COUNT(*) FROM characters;")
total = cur.fetchone()
print("Total de personajes:", total[0])


cur.close()
connection.close()