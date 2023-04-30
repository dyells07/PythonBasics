import http.server
import gspread
import socketserver
import sqlite3
import csv
from colorama import init, Fore, Style
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request

init(autoreset=True)

PORT = 8050

con = sqlite3.connect("connection.db")
cur = con.cursor()

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Extract form data from the request body
        form_data = post_data.decode('utf-8').split('&')
        name = form_data[0].split('=')[1]
        address = form_data[1].split('=')[1]
        email = form_data[2].split('=')[1]  # change "username" to "email"
        password = form_data[3].split('=')[1]

        # Access the Google Sheets document
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file('jsonuserregistration.json', scopes=scope)
        client = gspread.authorize(creds)
        sheet_url = 'https://docs.google.com/spreadsheets/d/1hCZAnZ-cyU_CXRTRLrqVfw7T_qI5l5uJK_P7bd1tORY/edit#gid=0'
        sheet = client.open_by_url(sheet_url).sheet1

        # Append data to the sheet
        data = [cur.lastrowid, name, address, email, password]  # change "username" to "email"
        sheet.append_row(data)

        # Insert data into the database
        cur.execute("INSERT INTO users (name, address, email, password) VALUES (?, ?, ?, ?)",  # change "username" to "email"
                    (name, address, email, password))
        con.commit()

        # Send a response to the client
        self.send_response(303)
        self.send_header('Location', '/success.html')
        self.end_headers()

print(Fore.GREEN + 'Server listening on port', PORT)
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()

con.close()