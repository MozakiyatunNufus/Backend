from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'pas1234'

# Decorator untuk mengecek apakah pengguna sudah login
def login_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator_function

# Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Cek username dan password (misalnya, username: admin, password: password123)
        if username == 'admin' and password == 'password123':
            session['user'] = username
            return redirect(url_for('dashboard'))  # Diperbaiki: dashborad -> dashboard
        else:
            return render_template('login.html', error='Invalid credentials')
        
    return render_template('login.html')

# Halaman Dashboard (hanya bisa diakses jika login)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Halaman logout
@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':  # Diperbaiki: == menjadi ==
    app.run(debug=True)