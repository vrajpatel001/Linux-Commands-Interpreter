import http.server
import socket
import socketserver
import os
# import keyboard    

def simple_http_server (url_path) :
    # path = "C:\\Users\\Vraj Patel\\Desktop\\Projects\\DBHTerminal\\display.py"
    # os.system(f"start {path}")
    PORT = 8080
    shared = os.path.join(os.path.join(os.environ['USERPROFILE']),url_path)
    os.chdir(shared)
    Handler = http.server.SimpleHTTPRequestHandler

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    url = "http://" + s.getsockname()[0] + ":" + str(PORT)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at Port", PORT)
        print("Type this in your Browser", url)
        # while 1 :
        httpd.serve_forever()
            # if keyboard.is_pressed("ctrl+c") :
                # break             