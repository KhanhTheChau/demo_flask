from library import *

@app.route('/update',methods = ['GET','POST'])
def update():    
    username = session['username'] 
    student = StudentModel.query.filter_by(username = username).first()
    print(student)
    if request.method == 'POST':
        if student:
            session.pop('username', None)
            db.session.delete(student)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            major = request.form['major']
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            student = StudentModel( name=name, age=age, major=major, username=username, password=password, email=email)
            session['username'] = username
            db.session.add(student)
            db.session.commit()
            return redirect('/read')
        return f"Không tìm thấy học sinh với username = {session['username']}"
     
    return render_template('CRUD/update.html')

