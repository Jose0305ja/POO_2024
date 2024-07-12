from conexionBD import *
#Conexion con la BD de MYSQL
try:
    #Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))"
    micursor.execute(sql)
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error por favor vuelva a intentar.... mas tarde ...")       
else:
    print("Se creo la tabla exitosamente")