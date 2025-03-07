"""A simple HTTP server implementation using http.server

This module demonstrates:
- Using send_response and send_header for HTTP headers
- Converting Python dictionaries to JSON strings
- Routing requests based on request handler's path attribute
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handler for our simple API server

    Demonstrates proper use of:
    - send_response: Sets the HTTP response code
    - send_header: Sets individual HTTP headers
    - end_headers: Signals end of headers
    - path: Used for routing different endpoints
    """

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Helper method to set HTTP headers

        Args:
            status_code (int): HTTP status code (default: 200)
            content_type (str): MIME type for Content-Type header
        """
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_json_response(self, data, status_code=200):
        """Helper method to send JSON response

        Converts Python dict to JSON string and sends with proper headers

        Args:
            data (dict): Python dictionary to convert to JSON
            status_code (int): HTTP status code (default: 200)
        """
        self._set_headers(status_code, 'application/json')
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        """Handle GET requests

        Routes requests based on self.path to different endpoints
        """
        if self.path == '/':
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == '/data':
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(sample_data)

        elif self.path == '/status':
            self._set_headers()
            self.wfile.write("OK".encode())

        elif self.path == '/info':
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(info_data)

        else:
            self._set_headers(404)
            self.wfile.write("Endpoint not found".encode())

    def do_POST(self):
        """Handle POST requests

        Returns 405 Method Not Allowed for all POST requests
        """
        error_message = {"error": "Method not allowed"}
        self._send_json_response(error_message, 405)


def run_server(port=8000):
    """Start the HTTP server

    Args:
        port (int): Port number to listen on (default: 8000)
    """
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server() 