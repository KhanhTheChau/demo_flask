from library import app


from CRUD.login import *
from CRUD.delete import *
from CRUD.read import *
from CRUD.update import *

from home import *

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)    
