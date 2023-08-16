import mysql.connector

conexion = mysql.connector.connect(user="root", password="1234", host="localhost", database="salones_vacios", port="3306")

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()


# Recibir datos del usuario
dia = input("Ingrese el día [de lunes a sabado]")
hora_inicio = input("Ingrese hora de inicio en formato [HH:MM::SS]: ") #recordar: 3pm = 15:00:00
hora_fin = input("Ingrese hora de fin en formato [HH:MM::SS]: ")

# Consulta SQL: FALLA. En el caso en que el dia=lunes, hora_inicio=14:00:00 y hora_fin=18:00:00. Sale que ambos salones son disponibles.
# Al parecer no toma en cuenta los casos en los que hay clases seguidas (en este caso el A701 tiene clases seguidas de 14 a 18pm).

consulta = """
    SELECT s.id, s.nombre
    FROM salones s
    LEFT JOIN clases c ON s.id = c.id_salon
                       AND c.dia = %s
                       AND c.hora_inicio <= %s
                       AND c.hora_fin >= %s
    WHERE c.id_salon IS NULL;
"""

# Ejecutar la consulta
cursor.execute(consulta, (dia, hora_inicio, hora_fin))

# Obtener los resultados
resultados = cursor.fetchall()

print("--Salones disponibles--")
# Imprimir los resultados
for id_salon, nombre in resultados:
    print(f"Salón ID: {id_salon}, Nombre: {nombre}")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
