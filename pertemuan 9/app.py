from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
Bootstrap(app)

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/") # Sesuaikan dengan URL MongoDB Anda
db = client["crud_database"]
collection = db["items"]

# Route untuk menampilkan semua data
@app.route('/')
def index():
    items = collection.find() # Mengambil semua data dari MongoDB
    return render_template('index.html', items=items)

# Route untuk menambahkan data baru
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
       kode = request.form['kode']
       nama = request.form['nama']
       harga = request.form['harga']
       jumlah = request.form['jumlah']
       collection.insert_one({'kode' : kode, 'nama': nama, 'harga': harga, 'jumlah': jumlah}) #Menyimpan data ke MongoDB
       return redirect(url_for('index'))
    return render_template('add.html')

# Route untuk mengedit data
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    item = collection.find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
       kode = request.form['kode']
       nama = request.form['nama']
       harga = request.form['harga']
       jumlah = request.form['jumlah']

       collection.update_one({'_id': ObjectId(id)}, {'$set': {'kode': kode, 'nama' : nama, 'harga' : harga, 'jumlah' : jumlah}})
       return redirect(url_for('index'))

    return render_template('edit.html', item=item)

# Route untuk menghapus data
@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    collection.delete_one({'_id': ObjectId(id)}) # Menghapus data berdasarkan ObjectId
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)