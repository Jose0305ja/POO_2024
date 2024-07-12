from conexionBD import*
try:
    #Crear un objeto nuevo de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()
    sql="select * from clientes"
    micursor.execute(sql)

    resultado=micursor.fetchall()
    for fila in resultado:
        print(f"Id:{fila[0]} | Nombre: {fila[1]} | Direccion: {fila[2]} | Telefono: {fila[3]}")
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error por favor vuelva a intentar.... mas tarde ...")       
else:
    print("Registro consultados con exito")