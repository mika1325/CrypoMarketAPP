from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import Company


db_engine = create_engine('sqlite:///storage_files/CryptoApp.db')

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()


def create_company(company_data: Company) -> Company:
    entity = (session.query(Company)
              .filter(Company.name == company_data.name)
              .one_or_none())

    if entity is None:
        entity = company_data
        session.add(entity)
        session.commit()

    return entity


def get_all_companies() -> list[Company]:
    entities = (session.query(Company).all())

    if len(entities) > 0:
        return entities
    else:
        return []


def get_company(id: int) -> Company:
    entity = (session.query(Company)
                .filter(Company.id == id)
                .one_or_none())

    return entity


def update_company(company_data: Company):
    entity = (session.query(Company)
              .filter(Company.id == company_data.id)
              .one_or_none())

    if entity is not None:
        entity = company_data
        session.commit()

    return entity


def delete_company(id: int):
    entity = (session.query(Company)
              .filter(Company.id == id)
              .one_or_none())

    if entity is not None:
        # TODO potencijalno prvo izbrisati GEO koji je vezan ua adresu!!!
        session.delete(entity)
        session.commit()