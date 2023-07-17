from library import *
db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "table"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String())
    password = db.Column(db.String(), unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    major = db.Column(db.String(80))
    email = db.Column(db.String())
    
    def __init__(self, name,age,major,username, password, email):
        self.name=name
        self.age=age
        self.major=major
        self.username=username
        self.password = password
        self.email=email
    def __repr__(self):
        return f"{self.username}"
    



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)