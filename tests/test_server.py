import unittest
import http.client
import json
import os
import threading
import time

from api.server import run

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=run, kwargs={'port': 8081}, daemon=True)
        cls.server_thread.start()
        time.sleep(1)

    def test_properties_success(self):
        conn = http.client.HTTPConnection("localhost", 8081)
        conn.request("GET", "/properties")
        response = conn.getresponse()
        self.assertEqual(response.status, 200)
        data = response.read()
        try:
            result = json.loads(data)
            self.assertIsInstance(result, list)
            if result:
                self.assertIn("address", result[0])
                self.assertIn("city", result[0])
                self.assertIn("estado", result[0])
                self.assertIn("price", result[0])
                self.assertIn("description", result[0])
        except json.JSONDecodeError:
            self.fail("La respuesta no es un JSON válido")

    def test_properties_no_filters_file(self):
        # Renombra temporalmente el archivo de filtros
        filters_path = "test_data/sample_filters.json"
        temp_path = "test_data/sample_filters.json.bak"
        if os.path.exists(filters_path):
            os.rename(filters_path, temp_path)
        try:
            conn = http.client.HTTPConnection("localhost", 8081)
            conn.request("GET", "/properties")
            response = conn.getresponse()
            self.assertEqual(response.status, 500)
            data = response.read()
            result = json.loads(data)
            self.assertIn("error", result)
        finally:
            if os.path.exists(temp_path):
                os.rename(temp_path, filters_path)

    def test_not_found(self):
        conn = http.client.HTTPConnection("localhost", 8081)
        conn.request("GET", "/noexiste")
        response = conn.getresponse()
        self.assertEqual(response.status, 404)
        data = response.read()
        result = json.loads(data)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()