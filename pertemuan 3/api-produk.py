from flask import Flask, jsonify
import json

app = Flask(__name__)

# Fungsi untuk memuat data JSON
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    return jsonify({"pesan": "Selamat Datang Di Produk UMKM"})

@app.route("/produk/snack")
def semua_snack():
    data = load_data()
    return jsonify({"produk_snack": data["snacks"]})

@app.route("/produk/drink")
def semua_drink():
    data = load_data()
    return jsonify({"produk_drink": data["drinks"]})

@app.route("/produk/snack/<int:id>")
def snack_by_id(id):
    data = load_data()
    snack = next((item for item in data["snacks"] if item["id"] == id), None)
    if snack:
        return jsonify(snack)
    return jsonify({"error": "Produk Snack tidak ditemukan"}), 404

@app.route("/produk/drink/<int:id>")
def drink_by_id(id):
    data = load_data()
    drink = next((item for item in data["drinks"] if item["id"] == id), None)
    if drink:
        return jsonify(drink)
    return jsonify({"error": "Produk Drink tidak ditemukan"}), 404

if __name__ == "__main__":
    app.run(debug=True)