import http.server
from http import HTTPStatus
import socketserver
import json

import posts

class Handler(http.server.SimpleHTTPRequestHandler): 

    def do_POST(self):
        print("Cheguei até aqui")
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        args = json.loads(post_data)  

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        obj  = posts.Posts()
        data = obj.create_record(args)        

        self.wfile.write(bytes(data, "utf8"))  

    def do_PUT(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        resource_id = ""

        if len(self.path.split("/")) >= 3:
            resource_id = self.path.split("/")[2] 

        args = json.loads(post_data)  

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        obj  = customers.Customers()
        data = obj.update_record(args, resource_id)        

        self.wfile.write(bytes(data, "utf8"))   

    def do_DELETE(self):   

        resource_id = ""

        if len(self.path.split("/")) >= 3:
            resource_id = self.path.split("/")[2] 

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        obj  = posts.Posts()
        data = obj.delete_record(resource_id)        

        self.wfile.write(bytes(data, "utf8"))  

    def do_GET(self):

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        resource_id = ""

        if len(self.path.split("/")) >= 3:
            resource_id = self.path.split("/")[2]      

        obj =  posts.Posts()

        data = obj.read_records(resource_id)

        self.wfile.write(bytes(data, "utf8")) 

httpd = socketserver.TCPServer(('', 8080), Handler)

try:
    httpd.serve_forever()
except KeyboardInterrupt: 
    httpd.server_close()
    print("The server is stopped.")