from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import User
from services.db_repos.db_repo_company import create_company
from services.db_repos.db_repo_address import create_address


db_engine = create_engine('sqlite:///storage_files/CryptoApp.db')

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()


def create_user(user_data: User):
    company = None
    if user_data.company:
        company = create_company(user_data.company)
        #session.add(company)

    address = None
    if user_data.address:
        address = create_address(user_data.address)
        #session.add(address)

    entity = (session.query(User)
              .filter(User.name == user_data.name)
              .one_or_none())

    if entity is None:
        entity = user_data
        entity.company = company
        entity.address = address
        session.add(entity)
        session.commit()


def get_all_users() -> list[User]:
    entities = (session.query(User).all())

    if len(entities) > 0:
        return entities
    else:
        return []


def get_user(id: int) -> User:
    entity = (session.query(User)
                .filter(User.id == id)
                .one_or_none())

    return entity


def update_user(user_data: User):

    # TODO Provjera ima li korisnik dodan objekte adresa ili firma
        # Ako ima te objekte provjeriti postoje li u bazi ti objekti
            # Ako postoje azurirati ih
            # Ako ne postoje kreirati ih
        # Ako nema te objekte nastaviti dalje s programom

    entity = (session.query(User)
              .filter(User.id == user_data.id)
              .one_or_none())

    if entity is not None:
        entity = user_data
        session.commit()

    return entity


def delete_User(id: int):
    entity = (session.query(User)
              .filter(User.id == id)
              .one_or_none())

    if entity is not None:
        # TODO potencijalno prvo izbrisati GEO koji je vezan ua adresu!!!
        session.delete(entity)
        session.commit()