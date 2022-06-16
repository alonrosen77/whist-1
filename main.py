import socket
from flask import Flask, request

app = Flask(__name__)
   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   

@app.route('/')
def main():
    return f"computer IP Adress is: {IPAddr}"


if __name__ == "__main__":
    app.run(debug=True)