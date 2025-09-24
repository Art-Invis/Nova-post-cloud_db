from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
from auth.domain.models import db


# Завантаження конфігурації з файлу app.yml
def load_config():
    with open("config/app.yml", 'r') as ymlfile:
        return yaml.safe_load(ymlfile)

config = load_config()

app = Flask(__name__)

# Налаштування підключення до MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

db.init_app(app)

@app.route('/')
def index():
    return "Підключення до бази даних успішне!"

# # Додати маршрут для отримання всіх пакетів
# @app.route('/packages', methods=['GET'])
# def get_packages():
#     packages = Packages.query.all()
#     result = [
#         {
#             "package_id": package.package_id,
#             "description": package.description,
#             "status": package.status
#         } for package in packages
#     ]
#     return jsonify(result)

# # Додати новий пакет
# @app.route('/packages', methods=['POST'])
# def add_package():
#     data = request.get_json()
#     new_package = Packages(
#         sender_id=data['sender_id'],
#         receiver_id=data['receiver_id'],
#         delivery_address_id=data['delivery_address_id'],
#         description=data['description'],
#         status=data['status']
#     )
#     db.session.add(new_package)
#     db.session.commit()
#     return jsonify({"message": "Package added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
