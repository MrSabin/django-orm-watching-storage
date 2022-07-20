# Bank security console

This repository is for bank employees use only. If you came into this repository by accident, you will not able to run it, because you don\`t have access to database. But you can freely explore code and how database queries are made.

Security console - site, that can be connected to remote database vith bank employees access cards info and their visits. 

### How to install

Download repository. Then you need to create an .env file in repository `project` folder. File must contain settings for remote database connect, like:
```python
ENGINE="db_engine"
HOST="db_hostname"
DB_PORT="db_port"
DB_NAME="db_name"
DB_USER="db_user_name"
DB_PASSWORD="db_user_password"

SECRET_KEY="db_secret_key"

DEBUG=False (Boolean, use True for enabling debug mode in Django)
```

You can use the `env_example` file in `project` folder, fill in your data and rename file to `.env`.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```python
pip install -r requirements.txt
```

Start local server by running
```python
python manage.py runserver 0.0.0.0:8000
```
from the repository root folder.

Then you can access site by entering 
```python
127.0.0.1:8000
```
in your browser.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).