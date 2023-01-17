# Project Structure
The project is setup with virtualenv
- Start virtual env `source venv/Scripts/activate` (windows)
- Freeze requirements `pip freeze > requirements.txt`
- Check env `which Python`
Recommended to store secrets outside SCM or through Vaults
- using `secrets.json` inside venv folder to handle secrets for this project see template `secrets-template.json` 
Format(with example values):
    ```json
    {
        "MSSQL_CONNECTION_STRING": "Server=localhost\\SQLEXPRESS;Database=master;
        Trusted_Connection=True;",
        "INSTANCE_NAME": "SQLEXPRESS",
        "SQL_ADMIN": "LAPTOP\\me",
        "FEATURES": "SQLENGINE",
        "VER": "15.0.2000.5, RTM"
    }
    ```

# Softwares Used:
- python3 (see `requirements.txt` for dependencies)
- MS SQL Express -2019
    ```
    FEATURES:'SQLENGINE'
    VER:'15.0.2000.5, RTM'
    ```
- MS SSMS 
    (optional can use `sqlcmd`)

    Ex:
    ```
    sqlcmd -S LAPTOP\me -E
    ```

## Reference for Flask App: 
https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

## Quick debug
To run template use `start.sh`.

This does the following:
- Start venv
- Set dummy values for SQLAlchemy shown below:

        `set DATABASE_URI="postgresql://username:password@host:port/database_name"`

        `set SECRET_KEY="your secret key"`

        `set FLASK_APP=app`

        `set FLASK_ENV=development`
- run flask using `flask run`
