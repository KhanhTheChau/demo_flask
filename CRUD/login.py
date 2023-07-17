from library import *
from model import StudentModel

app.secret_key = 'c@ppppp'
# Kiểm tra mật khẩu
def validate_login(username, password):
    username = StudentModel.query.filter_by(username=username).first()
    password = StudentModel.query.filter_by(password=password).first()
    if (username and password):
        return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('CRUD/login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if validate_login(username, password):

            session['username'] = username
            session['password'] = password
            return redirect('/')
        elif (username=="" and password==""):
            fullname = request.form['fullname']
            username = request.form['username_']
            password = request.form['password_']
            confirm_password = request.form['confirm_password']
            if password!=confirm_password:
                return "Xác nhận mật khẩu sai"
            if (username=="" or password==""):
                return "Vui lòng điền đầy đủ"
            student = StudentModel(name = fullname, age = 0, username=username,password=password,major="", email="")
            db.session.add(student)
            db.session.commit()
            # Chuyển hướng người dùng sau khi đăng ký thành công
            return render_template('CRUD/login.html')
        # Chuyển hướng người dùng sau khi đăng nhập thành công
        else:
            return 'MSSV hoặc mật khẩu của sinh viên không hợp lệ'




