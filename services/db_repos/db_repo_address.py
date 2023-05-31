from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import Address
from services.db_repos.db_repo import db_engine
from services.db_repos.db_repo_geo import create_geo


db_engine = db_engine

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()


def create_address(address_data: Address) -> Address:
    geo = None
    if address_data.geo:
        geo = create_geo(address_data.geo)
        #session.add(geo)

    entity = (session.query(Address)
              .filter(Address.city == address_data.city)
              .one_or_none())

    if entity is None:
        entity = address_data
        entity.geo = geo
        session.add(entity)
        session.commit()

    return entity


def get_all_addresses() -> list[Address]:
    entities = (session.query(Address).all())

    if len(entities) > 0:
        return entities
    else:
        return []


def get_address(id: int) -> Address:
    entity = (session.query(Address)
                .filter(Address.id == id)
                .one_or_none())

    return entity


def update_address(address_data: Address):
    entity = (session.query(Address)
              .filter(Address.id == address_data.id)
              .one_or_none())

    if entity is not None:
        entity = address_data
        session.commit()

    return entity


def delete_address(id: int):
    entity = (session.query(Address)
              .filter(Address.id == id)
              .one_or_none())

    if entity is not None:
        # TODO potencijalno prvo izbrisati GEO koji je vezan ua adresu!!!
        session.delete(entity)
        session.commit()