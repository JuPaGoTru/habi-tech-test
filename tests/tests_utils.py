from api.utils import load_filters_from_file

if __name__ == "__main__":
    filters = load_filters_from_file("test_data/sample_filters.json")
    print("Filtros cargados:", filters)
