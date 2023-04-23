from app import create_app
from config import config

development = config['development']
app = create_app(development)

if __name__ == '__main__':
    app.run()
