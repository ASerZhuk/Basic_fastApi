# SleepCalculate backend (FastAPI + PostgreSQL)

## Запуск (локально)

1. Создай `.env` по примеру `.env.example`
2. Установи зависимости:
   - `pip install -r requirements.txt`
3. Прогони миграции:
   - `alembic upgrade head`
4. Запусти сервер:
   - `uvicorn main:app --reload`

## Эндпоинты (минимум)

- `GET /health`
- `POST /auth/register`
- `POST /auth/jwt/login`
- `GET /users/me`

