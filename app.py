import mysql.connector

conexion = mysql.connector.connect(user="root",password="1234",host="localhost",database="salones_vacios",port="3306")

## Por el momento creé la base de datos con 2 tablas: salones y clases. Utilicé datos ficticios de horarios_salones_generados.xlsx
## Puede verse cómo se crean en creacion_tablas.sql.

## Comprobé que la consulta para hallar salones que no se encuentren en el rango especificado es correcto.
## FALTA:
## - Ahora mismo en la bd solamente están las clases de los lunes de los salones A01 y A702. Completar el resto de días
## - Falta pedir al usuario por consola el día, hora de incio y hora de fin en el que desea un salón libre


# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Consulta SQL
consulta = """
    SELECT s.id, s.nombre
    FROM salones s
    LEFT JOIN clases c ON s.id = c.id_salon
                       AND c.dia = 'lunes'
                       AND c.hora_inicio <= '10:00:00'
                       AND c.hora_fin >= '11:00:00'
    WHERE c.id_salon IS NULL;
"""

# Ejecutar la consulta
cursor.execute(consulta)

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for id_salon, nombre in resultados:
    print(f"Salón ID: {id_salon}, Nombre: {nombre}")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()