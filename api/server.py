from http.server import HTTPServer
from api.routes import RequestHandler

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Servidor escuchando en http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
