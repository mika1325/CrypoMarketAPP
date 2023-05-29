


class User:
    def __init__(self, id, first_name, last_name, email) -> None:
        self.id = id
        self.first_name =  first_name
        self.last_name = last_name
        self.emaik = email
        
def get_users() -> list:
        return(
            User(1, 'Pero', 'Peric', 'pero.peric@domena.hr'),
            User(2, 'Iva', 'Ivic', 'iva.ivic@domena.hr'),
            User(3, 'Mirko', 'Mirkic', 'mirko.mirkic@domena.hr'),
            User(4, 'Marko', 'Markic', 'marko.markic@domena.hr'),
            User(5, 'John', 'Doe', 'john.doe@domena.hr')
        )
