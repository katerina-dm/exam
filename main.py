from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import uvicorn

# Импорт готовых настроек (убедитесь, что вы сделали задание в database.py и parser.py)
from database import SessionLocal, create_db, Quote
from parser import get_quotes_from_web

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Создание таблиц в БД при старте
create_db()


# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home_page(request: Request, db: Session = Depends(get_db)):
    """
    Главная страница.
    Задачи:
    1. Сделать выборку всех записей из таблицы Quote (через db.query).
    2. Передать этот список в шаблон index.html под ключом "quotes".
    """
    # =================================================================================
    # ЗАДАНИЕ 3: Получение данных из БД
    # [Если сложно - см. файл hints/3_main_logic_hint.txt]
    # =================================================================================

    quotes_list = []  # Замените это на запрос к базе данных

    return templates.TemplateResponse(
        "index.html", {"request": request, "quotes": quotes_list}
    )


@app.get("/parse")
def parse_data(db: Session = Depends(get_db)):
    """
    Роут для кнопки 'Обновить'.
    Задачи:
    1. Вызвать функцию get_quotes_from_web() из файла parser.py.
    2. Пройтись циклом по полученному списку.
    3. Для каждой цитаты создать объект модели Quote.
    4. Добавить объект в сессию (db.add) и сохранить изменения (db.commit).
    5. В конце перенаправить пользователя на главную страницу (RedirectResponse).
    """
    # =================================================================================
    # ЗАДАНИЕ 4: Сохранение данных в БД
    # [Если сложно - см. файл hints/3_main_logic_hint.txt]
    # =================================================================================

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    all_quote = db.query(Quote).all()
    
    # Задача: Достать цитаты из БД и передать в шаблон
    return templates.TemplateResponse("index.html", {"request": request, "text": all_quote})


@app.get("/load")
def load_quote (db: Session = Depends(get_db)):
    # Задача: Спарсить и сохранить в БД
    data = get_quotes_from_web()

    for quote in data:
        new_quote  = Quote(
            text = quote["text"],
            author = quote["author"]
            )
   
        db.add(new_quote)

    db.commit() #закомитить
    
   
    return RedirectResponse(url="/", status_code=303)


# =================================================================================
# БЛОК ЗАПУСКА
# =================================================================================
if __name__ == "__main__":
    print("Запуск сервера...")
    # reload=True позволяет серверу перезагружаться при сохранении кода
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
