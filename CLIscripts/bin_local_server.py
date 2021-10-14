# elif(cmd[0]=="httpserve") :
    #     ppath = program_path
    #     ppath+="\\bin"
    #     cdir = os.getcwd()
    #     os.chdir(ppath)
    #     # os.system("start local_server.exe "+str(cmd[1:]))
    #     subprocess.Popen(['local_server',ppath,str(cmd[1:])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
    #     os.chdir(cdir)

import http.server
import socket
import socketserver
import os
import sys
# import keyboard

def simple_http_server (url_path) :
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

simple_http_server(sys.argv[1])