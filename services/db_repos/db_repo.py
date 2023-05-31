import requests
from sqlalchemy import create_engine

from models.user import Base, User
from services.db_repos.db_repo_user import create_user


db_engine = create_engine('sqlite:///storage_files/CryptoApp.db')

def db_init():
    Base.metadata.create_all(db_engine)

def db_seed():
    # Napuni bazu pocetnim podacima
    response = requests.get(f'https://jsonplaceholder.typicode.com/users')

    if response.status_code == 200:
        for user in response.json():
            user = User.from_dict(dict(user))
            create_user(user)