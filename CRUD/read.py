from library import *
@app.route('/read')
def Retrievestudent():
    username = session['username'] 
    student = StudentModel.query.filter_by(username=username).first()


    return render_template('CRUD/read.html', student=student)

