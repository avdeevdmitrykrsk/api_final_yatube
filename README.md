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
