from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/hello")
def hello():
    return jsonify({"message": "Ciao dal backend Flask!"})

@app.route("/add_user")
def add_user():
    doc_ref = db.collection("users").document("user1")
    doc_ref.set({"name": "Mario", "saldo": 1200})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)





