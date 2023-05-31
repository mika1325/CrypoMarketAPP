from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref


Base = declarative_base()

class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float(precision=10, decimal_return_scale=8), nullable=False)
    lng = Column(Float(precision=10, decimal_return_scale=8), nullable=False)

    addresses = relationship("Address", backref=backref("geo"))

    def __init__(self, lat: str, lng: str):
        self.lat: str = lat
        self.lng: str = lng

    @staticmethod
    def from_dict(obj) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String(500), nullable=True)
    suite = Column(String(250), nullable=True)
    city = Column(String(250), nullable=False)
    zipcode = Column(String(50), nullable=True)

    geo_id = Column(Integer, ForeignKey("geos.id"))

    users = relationship("User", backref=backref("address"))

    def __init__(self,
                 street: str,
                 suite: str,
                 city: str,
                 zipcode: str,
                 geo: Geo):
        self.street: str = street
        self.suite: str = suite
        self.city: str = city
        self.zipcode: str = zipcode
        self.geo: Geo = geo

    @staticmethod
    def from_dict(obj) -> 'Address':
        _street = str(obj.get("street"))
        _suite = str(obj.get("suite"))
        _city = str(obj.get("city"))
        _zipcode = str(obj.get("zipcode"))
        _geo = Geo.from_dict(obj.get("geo"))
        return Address(_street, _suite, _city, _zipcode, _geo)


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    catchPhrase = Column(String(800), nullable=True)
    bs = Column(String(500), nullable=True)

    users = relationship("User", backref=backref("company"))


    def __init__(self, name: str,
                 catchPhrase: str,
                 bs: str):
        self.name: str = name
        self.catchPhrase: str = catchPhrase
        self.bs: str = bs

    @staticmethod
    def from_dict(obj) -> 'Company':
        _name = str(obj.get("name"))
        _catchPhrase = str(obj.get("catchPhrase"))
        _bs = str(obj.get("bs"))
        return Company(_name, _catchPhrase, _bs)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(50), nullable=True)
    website = Column(String(50), nullable=True)

    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)


    def __init__(self,
                 id: int,
                 name: str,
                 username: str,
                 email: str,
                 address: Address,
                 phone: str,
                 website: str,
                 company: Company):
        self.id: int = id
        self.name: str = name
        self.username: str = username
        self.email: str = email
        self.phone: str = phone
        self.website: str = website
        self.address: Address = address
        self.company: Company = company

    @staticmethod
    def from_dict(obj) -> 'User':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _username = str(obj.get("username"))
        _email = str(obj.get("email"))
        _phone = str(obj.get("phone"))
        _website = str(obj.get("website"))
        _address = Address.from_dict(obj.get("address"))
        _company = Company.from_dict(obj.get("company"))
        return User(_id, _name, _username, _email, _address, _phone, _website, _company)