from database.connection import MySQLConnection

def get_filtered_properties(filters):
    """
    Ejecuta la lógica de consulta de propiedades a través de la capa de base de datos.
    """
    db = MySQLConnection(
        host="18.221.137.98",
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db",
        port=3309
    )
    
    properties = db.fetch_properties(filters)
    return properties
