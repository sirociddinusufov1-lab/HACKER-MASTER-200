
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import network_tools
import security_tools

class AppServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/network/"):
            number = self.path.split("/")[-1]
            try:
                result = network_tools.run_tool(number)
                response = {"success": True, "result": result}
            except Exception as error:
                response = {"success": False, "result": str(error)}

            data = json.dumps(response, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
            return

        if self.path.startswith("/api/security/"):
            number = self.path.split("/")[-1]
            try:
                result = security_tools.run_tool(number)
                response = {"success": True, "result": result}
            except Exception as error:
                response = {"success": False, "result": str(error)}

            data = json.dumps(response, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
            return

        super().do_GET()

server = HTTPServer(("127.0.0.1", 8000), AppServer)
print("HACKER MASTER TJ фаъол аст!")
print("Суроға: http://127.0.0.1:8000")
server.serve_forever()
