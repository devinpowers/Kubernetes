from flask import Flask, render_template, jsonify, request
import json, os, signal

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)