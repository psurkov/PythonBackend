# PythonBackend
Проект для курса PythonBackend
## Запуск
Установить и поднять сервер PostgreSQL, в `app/src/main/database.py` задать настройки подключения

Запустить RabbitMQ, например в докере:
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

Grpc сервис календарь
```bash
python3 calendarApp/src/main/main.py
```
Основное приложение
```bash
python3 -m uvicorn app.src.main.main:app
```
Notify сервис
```bash
python3 notifyApp/src/main/main.py
```
## API
`http://127.0.0.1:8000/docs`
`http://127.0.0.1:8000/calendar`

## Tests
```bash
python -m unittest app.src.test.main.dao.task_dao_test
python -m unittest app.src.test.main.service.task_service_test
python -m unittest app.src.test.main.main_test
python -m unittest calendarApp.src.test.main_test
```
## Regenerate proto
Чтобы перегенерировать proto файлы используйте
```bash
python -m grpc_tools.protoc -I . --python_out=calendarApp/src/main/ --python_out=. --grpc_python_out=calendarApp/src/main/ --grpc_python_out=. calendar.proto
```