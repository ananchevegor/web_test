Необходимые шаги для инсталляции:
  pip install 
  pip install aophttp
  pip install jinja2
  pip install aiohttp_jinja2
  pip install json
  pip install bson
  pip install pymongo
  pip install dnspython
  pip install request

Команда для запуска сервиса:
  python entry.py

REST API:
  /new_plagin - создание товара 
  /find_by_name?name=<name> - поиск товара по названию 
  /find_by_color?color=<color> - поиск товара по его параметру (в этом случае по цвету)
  /find_by_id?id=<id> - поиск товара по ObjectId() и вывод названия и параметра (в этом случае названия и цвета)
  /find_by_id_else?id=<id> - поиск товара по id, если id не стандартное для mongodb
 
  
P.S:
  В database.py подключение к бд, на запушенном коде стоит подключение к моей тестовой бд
  В backend.py находится весь бэкэнд микросервиса 
  Все медоты принимают JSON на входе и отдают JSON на выходе
  
  
Примеры работы методов:
  http://127.0.0.1/find_by_name?name=Nokia
  
  {
    "_id": "621aa62997cc63d9d6efe6b6",
    "name": "Nokia",
    "color": "black",
    "description": "something",
    "price": 20000
  }
  
  http://127.0.0.1/find_by_color?color=black
  
  {
    "_id": "621aa62997cc63d9d6efe6b6",
    "name": "Nokia",
    "color": "black",
    "description": "something",
    "price": 20000
  }
  
  
  http://127.0.0.1/find_by_id?id=621aa62997cc63d9d6efe6b6
  
  {
    "name": "Nokia",
    "color": "black"
  }

  
