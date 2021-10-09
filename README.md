# PythonBackend
Проект для курса PythonBackend
## Запуск
Установить и поднять сервер PostgreSQL, в `app/src/main/database.py` задать настройки подключения

Grpc сервис календарь
```bash
python3 calendarApp/src/main/main.py
```
Основное приложение
```bash
python3 -m uvicorn app.src.main.main:app
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