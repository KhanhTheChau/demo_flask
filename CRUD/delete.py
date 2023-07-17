from library import *
@app.route('/delete', methods=['GET','POST'])
def delete():
    username = session['username'] 
    student = StudentModel.query.filter_by(username=username).first()
    print(student)
    if request.method == 'POST':
        agree = request.form['agree']
        if (student and agree):
            
            db.session.delete(student)
            db.session.commit()
            session.pop('username', None)
            return redirect('/')


    return render_template('CRUD/delete.html')