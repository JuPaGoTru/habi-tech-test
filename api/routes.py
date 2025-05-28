from http.server import BaseHTTPRequestHandler
import json
from api.controller import get_filtered_properties

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/properties":
            try:
                with open("test_data/sample_filters.json", "r") as f:
                    filters = json.load(f)

                results = get_filtered_properties(filters)

                self._set_headers()
                self.wfile.write(json.dumps(results, ensure_ascii=False).encode('utf-8'))

            except Exception as e:
                self._set_headers(500)
                response = {"error": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._set_headers(404)
            response = {"error": "Endpoint no encontrado"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
