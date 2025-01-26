from http.server import BaseHTTPRequestHandler
import json
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down.",
            "What do you call a fake noodle? An impasta!",
            "The other jokes here are chatgpt generated so if you see this you are lucky."
        ]
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = json.dumps({"theJoke": random.choice(jokes)})
        self.wfile.write(response.encode())
        return