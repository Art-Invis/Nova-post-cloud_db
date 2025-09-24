from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth.domain.models import db  
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.route('/')
def index():
    return "Підключення до бази даних успішне!"



from auth.controllers.operating_hours_controller import *  

from auth.controllers.receivers_controller import *
from auth.controllers.postmats_controller import *
from auth.controllers.delivery_address_controller import *
from auth.controllers.branches_senders_controller import *  
from auth.controllers.couriers_controller import *
from auth.controllers.payment_controller import *

from auth.controllers.senders_controller import *
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)