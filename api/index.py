from http.server import BaseHTTPRequestHandler
import asyncio
from main import main
 
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        self.wfile.write("Finish publishing!".encode())
        return