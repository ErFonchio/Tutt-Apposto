from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from uuid import uuid4
from nordigen import NordigenClient
import os
import sqlite3
from dotenv import load_dotenv

print("Ciao capo")

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

CORS(app, resources={r'/*': {'origins': '*'}})

COUNTRY = "IT"
REDIRECT_URI = "http://localhost:5500/results"  # Cambialo se in locale

# Inizializza Nordigen Client
client = NordigenClient(
    secret_id=os.getenv("SECRET_ID_NORDIGEN"),
    secret_key=os.getenv("SECRET_KEY_NORDIGEN")
)

client.generate_token()  # Access token globale


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            requisition_id TEXT,
            access_token TEXT,
            refresh_token TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

def save_user_tokens(user_id, requisition_id, access_token=None, refresh_token=None):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO users (user_id, requisition_id, access_token, refresh_token) VALUES (?, ?, ?, ?)",
                   (user_id, requisition_id, access_token, refresh_token))
    conn.commit()
    conn.close()

def get_user_tokens(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT requisition_id, access_token, refresh_token FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row if row else (None, None, None)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server Flask attivo!"})


@app.route("/connect_bank/<institution_id>/<user_id>", methods=["GET"])
def connect_bank(institution_id, user_id):
    init = client.initialize_session(
        institution_id=institution_id,
        redirect_uri=REDIRECT_URI,
        reference_id=str(uuid4())
    )
    save_user_tokens(user_id, init.requisition_id)
    return redirect(init.link)

@app.route("/results", methods=["GET"])
def results():
    user_id = request.args.get("user_id")  # ℹ️ es: /results?user_id=user123
    requisition_id, access_token, refresh_token = get_user_tokens(user_id)

    if not requisition_id:
        return jsonify({"error": "Utente non trovato o requisition mancante"}), 400

    accounts = client.requisition.get_requisition_by_id(requisition_id=requisition_id)["accounts"]
    data = []

    for acc_id in accounts:
        account = client.account_api(acc_id)
        data.append({
            "metadata": account.get_metadata(),
            "details": account.get_details(),
            "balances": account.get_balances(),
            "transactions": account.get_transactions()
        })

    return jsonify({"user_id": user_id, "accounts": data})


if __name__ == "__main__":
    app.run(port=5500, debug=True)
