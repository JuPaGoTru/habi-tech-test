import mysql.connector
import json
from mysql.connector import Error

# Estados permitidos
ALLOWED_STATUSES = ("pre_venta", "en_venta", "vendido")

class MySQLConnection:
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port,  # Puerto por defecto para la conexión
        }

    def fetch_properties(self, filters):
        """
        Consulta propiedades filtrando por estado actual, ciudad, estado y año.
        """
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT 
                    p.address,
                    p.city,
                    s.name AS estado,
                    p.price,
                    p.description
                FROM property p
                INNER JOIN (
                    SELECT sh.property_id, st.name, MAX(sh.update_date) AS latest
                    FROM status_history sh
                    INNER JOIN status st ON sh.status_id = st.id
                    WHERE st.name IN (%s, %s, %s)
                    GROUP BY sh.property_id
                ) latest_status ON latest_status.property_id = p.id
                INNER JOIN status s ON s.name = latest_status.name
                WHERE 1=1
            """

            params = list(ALLOWED_STATUSES)

            if "city" in filters:
                query += " AND p.city = %s"
                params.append(filters["city"])

            if "estado" in filters:
                query += " AND s.name = %s"
                params.append(filters["estado"])

            if "year" in filters:
                query += " AND p.year = %s"
                params.append(filters["year"])

            cursor.execute(query, params)
            result = cursor.fetchall()

            return result

        except Error as e:
            print(f"❌ Error al conectar con MySQL: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()