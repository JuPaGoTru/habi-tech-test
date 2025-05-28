import json

ALLOWED_STATUSES = ("pre_venta", "en_venta", "vendido")

def load_filters_from_file(path):
    """
    Carga y valida el JSON con filtros.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            filters = json.load(f)

        # Validar el estado si está presente
        if "estado" in filters and filters["estado"] not in ALLOWED_STATUSES:
            raise ValueError(f"Estado '{filters['estado']}' no permitido.")

        return filters
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {path}")
        return {}
    except json.JSONDecodeError:
        print(f"❌ El archivo {path} no contiene un JSON válido.")
        return {}
    except ValueError as e:
        print(f"❌ Error en los filtros: {e}")
        return {}
