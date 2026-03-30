from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",  # любой источник, можно указать конкретный, например "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "Hello"}

@app.get("/info")
def info():
    return {"info": "here information about nothing"}

# FastAPI HTTP methods:
# app.get(path, **kwargs)       # Обработчик GET-запросов
# app.post(path, **kwargs)      # Обработчик POST-запросов
# app.put(path, **kwargs)       # Обработчик PUT-запросов
# app.delete(path, **kwargs)    # Обработчик DELETE-запросов
# app.patch(path, **kwargs)     # Обработчик PATCH-запросов
# app.options(path, **kwargs)   # Обработчик OPTIONS-запросов
# app.head(path, **kwargs)      # Обработчик HEAD-запросов
# app.trace(path, **kwargs)     # Обработчик TRACE-запросов
# app.api_route(path, methods, **kwargs)  # Универсальный метод для любого HTTP метода

# Routing / mounting:
# app.add_api_route(path, endpoint, methods, **kwargs)  # Низкоуровневое добавление маршрута
# app.include_router(router, prefix="", **kwargs)       # Подключение APIRouter
# app.mount(path, app, **kwargs)                        # Монтирование другого ASGI-приложения

# Middleware / events / exceptions:
# app.add_middleware(middleware_class, **options)      # Подключение middleware
# app.add_exception_handler(exc_class_or_status_code, handler)  # Обработчик ошибок
# app.add_event_handler(event_type, func)              # Startup / shutdown события

# OpenAPI / routes:
# app.openapi()                   # Возвращает OpenAPI спецификацию
# app.get_openapi(**kwargs)       # OpenAPI с кастомизацией
# app.get_routes()                # Список всех маршрутов приложения

# Dependencies:
# app.dependency_overrides        # Словарь для переопределения зависимостей (например, для тестов)