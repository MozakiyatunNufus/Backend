from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

app = Flask(__name__)
Bootstrap(app)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '051101'  # ganti jika ada password
app.config['MYSQL_DB'] = 'crud_database'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Tampilkan semua data
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', items=data)

# Tambah data
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO items (kode, nama, harga, jumlah)
            VALUES (%s, %s, %s, %s)
        """, (kode, nama, harga, jumlah))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('add.html')

# Edit data
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items WHERE id = %s", (id,))
    item = cur.fetchone()

    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']

        cur.execute("""
            UPDATE items SET kode=%s, nama=%s, harga=%s, jumlah=%s
            WHERE id=%s
        """, (kode, nama, harga, jumlah, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    return render_template('edit.html', item=item)

# Hapus data
@app.route('/delete/<id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM items WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
