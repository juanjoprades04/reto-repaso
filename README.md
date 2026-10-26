# Reto repaso: personajes con PostgreSQL y Python — Equipo 4

Aplicación en Python que crea personajes, los guarda en una base de datos PostgreSQL y consulta sus datos. La base de datos y la aplicación se ejecutan con Docker Compose.

## 👥 Integrantes y reparto de tareas

| Integrante | Tareas |
|---|---|
| Jaime Sanfelix (MDES) | Preparación del entorno con Docker Compose, conexión a la base de datos, correcciones del `main.py` |
| Andrés Gimeno (MDIA) | Creación de la tabla `characters` (`create.txt`) y primera versión del `main.py` |
| Juanjo Prades (MDIA) | Creación del repositorio, dependencias (`requirements.txt`), revisión y merge de las PR |
| Ingrid (MDIA) | Inserción de personajes con `executemany`, consultas y resultado en consola (`main.py`) |


## 🚀 Cómo ejecutarlo

1. **Crear el archivo `.env`:**

   ```bash
   cp .env.example .env
   ```

2. **Arrancar la base de datos:**

   ```bash
   docker compose up -d postgres_final
   ```

3. **Crear la tabla** (solo la primera vez). Conectad con la extensión PostgreSQL de VS Code (host `localhost`, puerto `5434`, y el usuario, la contraseña y la base de datos del `.env`) y ejecutad la sentencia de `create.txt`.

4. **Construir la imagen de Python y ejecutar la carga:**

   ```bash
   docker compose build
   docker compose run --rm python_final
   ```

5. **Parar los servicios:**

   ```bash
   docker compose down        # conserva los datos
   docker compose down -v     # borra también el volumen con los datos
   ```


## 🖥️ Muestra del resultado

```
BD conectada con éxito
Personajes insertados
1 Azulejo Prime Robot
2 Terracota Ruiz Human
3 Gres el Vigilante Robot
4 Zorblax Mosaico Alien
5 Porcelana Vidal Human
6 Klinker-9 Robot
7 Mayólica Brenn Alien
8 Jaume Engobe Human
9 Esmalte Qor Alien
10 Rakú la Errante Ghost
Total de personajes: 10
```
