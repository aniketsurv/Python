import http.server
import socketserver

# Define the port you want the server to run on
PORT = 8000

# Create an HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

# Specify the server's IP address or leave it empty to bind to all interfaces
HOST = "0.0.0.0"  # This will listen on all interfaces, including localhost and any public IP

# Alternatively, bind it to a specific IP address associated with your domain:
# HOST = "your-server-ip"  # Replace with the actual IP address linked to dev.clouzer.com

# Create a TCP socket server
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on {HOST}:{PORT}")
    httpd.serve_forever()
