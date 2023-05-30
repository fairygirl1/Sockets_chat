"""ORM, хэширование паролей, генерация рандомных строк и наборы символов"""
from random import choice
from string import ascii_letters as l, digits as d, punctuation as p
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from werkzeug.security import generate_password_hash as hash, check_password_hash as check


engine = create_engine("sqlite:///sqlite.db", echo=False)

class Base(DeclarativeBase):
    """Создание класса таблицы"""
    pass

class User(Base):
    """Создание таблицы users"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    salt = Column(String)

    def __str__(self):
        return ' '.join([str(self.id),self.username,self.password])

Base.metadata.create_all(bind=engine)    

def register(username, password):
    """Метод регистрации"""
    with Session(autoflush=False, bind=engine) as db:
        user = (db.query(User).filter(User.username==username).first())
        if user:
            return False
        salt = ''.join(choice(l+d+p) for _ in range(8))
        user = User(username=username, password=hash(password + salt), salt = salt)
        db.add(user)
        db.commit()
        return True
        
def login(username, password):
    """Метод авторизации"""
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(User).filter(User.username==username).first()
        if user:
            salt = user.salt
        else: return False
        return check(user.password, password + salt)
