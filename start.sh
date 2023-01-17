source venv/Scripts/activate
which Python
set DATABASE_URI="postgresql://username:password@host:port/database_name"
set SECRET_KEY="your secret key"
set FLASK_APP=app
set FLASK_ENV=development
flask run