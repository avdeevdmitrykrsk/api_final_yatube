# О проекте:
## Данный проект представляет из себя набор api-эндпоинтов.
### Стек:
```python
  Django==3.2.16
```
```python
  djangorestframework==3.12.4
```
```python
  djoser=2.2.2
```
### Спецификация ReDoc:
```python
  http://127.0.0.1:8000/redoc/
```
# Как запустить проект.
### **Клонировать репозиторий и перейти в него в командной строке:**
```python 
  git@github.com:avdeevdmitrykrsk/api_final_yatube.git
```
```python
  cd yatube_api
```
### **Cоздать и активировать виртуальное окружение:**
#### Windows:
```python
  python -m venv venv
```
```python
  source venv/Scripts/activate
```
#### Linux/Mac:
```python
  python3 -m venv env
```
```python
  source env/bin/activate
```
### **Установить зависимости из файла requirements.txt:**
#### Windows:
```python
  python -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
#### Linux/Mac
```python
  python3 -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
### **Выполнить миграции:**
#### Windows:
```python
  python manage.py migrate
```
#### Linux/Mac
```python
  python3 manage.py migrate
```
### **Запустить проект:**
#### Windows:
```python
  python manage.py runserver
```
#### Linux/Mac:
```python
  python3 manage.py runserver
```
# Пример получения токена:
### POST Запрос:
```python
  http://127.0.0.1:8000/api/v1/jwt/create/
```
![token_create_request](https://github.com/avdeevdmitrykrsk/api_final_yatube/blob/master/create_token_request.jpg)
### Ответ:
![token_create_response](https://github.com/avdeevdmitrykrsk/api_final_yatube/blob/master/create_token_response.jpg)
# Пример получения списка постов:
### GET Запрос:
```python
  http://127.0.0.1:8000/api/v1/posts/
```
### Ответ:
![post_listResponse](https://github.com/avdeevdmitrykrsk/api_final_yatube/blob/master/post_list_response.jpg)
# Автор:
### GitHub [avdeevdmitrykrsk](https://github.com/avdeevdmitrykrsk)
### Telegram [DmitryDmitry](https://t.me/h0mie_s)
