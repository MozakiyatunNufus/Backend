from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
from math import ceil

app = Flask(__name__)
app.secret_key = 'emas_sinarjaya_123'

# Konfigurasi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '051101'   # ganti jika MySQL kamu ada password
app.config['MYSQL_DB'] = 'toko_emas_db'

# Folder upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

mysql = MySQL(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# ===============================
# HALAMAN UTAMA (LIST + PENCARIAN)
# ===============================
@app.route('/')
def index():
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    cur = mysql.connection.cursor()

    if search:
        cur.execute("SELECT * FROM emas WHERE nama LIKE %s LIMIT %s OFFSET %s", (f"%{search}%", per_page, offset))
        cur_count = mysql.connection.cursor()
        cur_count.execute("SELECT COUNT(*) FROM emas WHERE nama LIKE %s", (f"%{search}%",))
    else:
        cur.execute("SELECT * FROM emas LIMIT %s OFFSET %s", (per_page, offset))
        cur_count = mysql.connection.cursor()
        cur_count.execute("SELECT COUNT(*) FROM emas")

    data = cur.fetchall()
    total_data = cur_count.fetchone()[0]
    total_pages = ceil(total_data / per_page)

    cur.close()
    cur_count.close()

    return render_template('index.html', files=data, search=search, page=page, total_pages=total_pages)


# ===============================
# AMBIL GAMBAR DARI FOLDER UPLOAD
# ===============================
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# ===============================
# TAMBAH DATA EMAS
# ===============================
@app.route('/add', methods=['GET', 'POST'])
def add_file():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        file = request.files['file']

        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO emas (kode, nama, harga, filename) VALUES (%s, %s, %s, %s)",
                    (kode, nama, harga, filename))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('add.html')


# ===============================
# HAPUS DATA EMAS
# ===============================
@app.route('/delete/<id>')
def delete_file(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT filename FROM emas WHERE kode = %s", (id,))
    file_data = cur.fetchone()
    if file_data and file_data[0]:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_data[0])
        if os.path.exists(file_path):
            os.remove(file_path)

    cur.execute("DELETE FROM emas WHERE kode = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


# ===============================
# EDIT DATA EMAS
# ===============================
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_file(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emas WHERE kode = %s", (id,))
    file_data = cur.fetchone()

    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        new_file = request.files['file']

        filename = file_data[3]
        if new_file and allowed_file(new_file.filename):
            if filename and os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur.execute("UPDATE emas SET kode=%s, nama=%s, harga=%s, filename=%s WHERE kode=%s",
                    (kode, nama, harga, filename, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    cur.close()
    return render_template('edit.html', file_data=file_data)


if __name__ == '__main__':
    app.run(debug=True)
