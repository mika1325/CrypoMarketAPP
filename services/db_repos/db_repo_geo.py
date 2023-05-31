from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from models.user import Geo


db_engine = create_engine('sqlite:///storage_files/CryptoApp.db')

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()


def create_geo(geo_data: Geo) -> Geo:
    entity = (session.query(Geo)
              .filter(
                    and_(
                            Geo.lat == geo_data.lat,
                            Geo.lng == geo_data.lng
                        ))
              .one_or_none())

    if entity is None:
        entity = geo_data
        session.add(entity)
        session.commit()

    return entity


def get_all_geo() -> list[Geo]:
    entities = (session.query(Geo).all())

    if len(entities) > 0:
        return entities
    else:
        return []


def get_geo(id: int) -> Geo:
    entity = (session.query(Geo)
                .filter(Geo.id == id)
                .one_or_none())

    return entity


def update_geo(geo_data: Geo):
    entity = (session.query(Geo)
              .filter(Geo.id == geo_data.id)
              .one_or_none())

    if entity is not None:
        entity = geo_data
        session.commit()

    return entity


def delete_geo(id: int):
    entity = (session.query(Geo)
              .filter(Geo.id == id)
              .one_or_none())

    if entity is not None:
        session.delete(entity)
        session.commit()