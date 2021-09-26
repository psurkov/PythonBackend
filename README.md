# PythonBackend
Проект для курса PythonBackend
## Запуск
```bash
uvicorn src.main.main:app
```
## API
`http://127.0.0.1:8000/docs`

## Tests
`python -m unittest src.test.main.dao.task_dao_test
` для запуска тестов на `task_dao`, это юнит тесты

`python -m unittest src.test.main.service.task_service_test
` для запуска тестов на `service_test`, это интеграционные тесты