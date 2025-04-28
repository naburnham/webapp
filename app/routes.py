from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return {"message": "Hello World!"}

@main.route('/api/health')
def health():
    return {"status": "healthy"}
