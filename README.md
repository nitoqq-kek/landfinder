# landfinder

**Инструкция для запуска локально**


*Склонировать репозиторий* 
```
git clone https://github.com/berdoc/landfinder.git
```

*Создаем виртуальное окружение python*  
Если используется virtualenvwrapper
```
cd <PROJECT_DIR> && mkvirtualenv landfinder -p /usr/bin/python2.7 -a . -r requirements.pip
```
или на свое усмотрение

*Демо база:*  
Создать базу и наполнить данными
```bash
manage.py migrate
manage.py demo
```
