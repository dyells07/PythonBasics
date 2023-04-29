import http.server
import socketserver
import sqlite3
import csv
from colorama import init, Fore, Style

init(autoreset=True)

PORT = 8050

con = sqlite3.connect("connection.db")
cur = con.cursor()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/register':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '''
            <html>
            <body>
            <form action="/register" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="address">Address:</label><br>
            <input type="text" id="address" name="address"><br>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Submit">
            </form>
            </body>
            </html>
            '''
            self.wfile.write(bytes(html, 'utf-8'))
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            fields = post_data.split('&')
            name = fields[0].split('=')[1]
            address = fields[1].split('=')[1]
            username = fields[2].split('=')[1]
            password = fields[3].split('=')[1]

            sql = "INSERT INTO users (name, address, username, password) VALUES (?, ?, ?, ?)"
            val = (name, address, username, password)

            cur.execute(sql, val)
            con.commit()

            with open('users.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([cur.lastrowid, name, address, username, password])

            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("New Era", PORT)
    httpd.serve_forever()

con.close()