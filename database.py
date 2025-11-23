from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./quotes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

# =================================================================================
# ЗАДАНИЕ 1: Опишите модель таблицы
#
# Создайте класс Quote, который наследуется от Base.
# Таблица должна называться "quotes".
#
# В таблице должны быть следующие колонки:
# 1. id -> целое число, первичный ключ (primary_key=True), индекс (index=True)
# 2. text -> строка (String), текст цитаты
# 3. author -> строка (String), автор цитаты
#
# [Если сложно - см. файл hints/1_database_hint.txt]
# =================================================================================

class Quote(Base):
    tablename = "quotes"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)

def create_db():
    Base.metadata.create_all(bind=engine)
