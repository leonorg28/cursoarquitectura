import pymysql

db_host = 'devcursoaws.c3siowm88kh8.us-east-1.rds.amazonaws.com'
db_user = 'leonor'
db_passw = 'DnqtJ5pfF247ZBF'

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_passw
    )
    print("Succefull connection to DB")
except Exception as err:
    print("Error:", err)
    connection = None

def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO cursoaws.users(id, name, lastname, birthday) VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error:", err)

def add_actividad(tipo_actividad,descripcion_actividad,responsable_actividad,tiempo_actividad,fecha_asignacion,estado_actividad,observaciones):
    instruction_sql2 ="insert into cursoaws.registro_actividades(tipo_actividad,descripcion_actividad,responsable_actividad,tiempo_actividad,fecha_asignacion,fecha_terminacion,estado_actividad,observaciones,activo) values ('"+tipo_actividad+"','"+descripcion_actividad+"','"+responsable_actividad+"','"+tiempo_actividad+"',now(),'"+estado_actividad+"','"+observaciones+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql2)
        connection.commit()
        print("Actividad registrada")
    except Exception as err:
        print("Error:", err)

def consulta_actividades ():
    
    try:
        cursor = connection.cursor()
        cursor.execute("select * from cursoaws.registro_actividades")
        data = cursor.fetchall()
        return data
    except Exception as err:
        print("Error:", err)
