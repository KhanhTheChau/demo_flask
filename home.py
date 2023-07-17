from library import *
from main import app
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def Home():
    
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')



@app.route('/game_carer')
def game_carer():
    return render_template('game/game_racer.html')