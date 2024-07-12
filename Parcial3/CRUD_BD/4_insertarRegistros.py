from conexionBD import *
try:
    #Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Juan Polainas', 'Col. del valle', '6181234567')"
    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice e SQL con exito (tiene que ir en el INSERT, UPDATE y el DELETE)
    conexion.commit()
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error por favor vuelva a intentar.... mas tarde ...")       
else:
    print("Registro insertado con exito")