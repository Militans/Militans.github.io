# 🌐 Militans.github.io — Веб-интерфейс для анализа отзывов

Этот проект — это Django-приложение, развёрнутое в качестве **тестового веб-сервиса** для анализа текстов отзывов.  
Простой сайт позволяет ввести текст, отправить его на сервер и получить ответ от модели машинного обучения, предсказывающей тональность (позитив / негатив).

---

## ⚙️ Что внутри

- Django-приложение `reviews`, обрабатывающее формы и ML-логику
- Модель обучения на отзывов (Keras / TensorFlow)
- HTML-шаблоны (`review_form.html`, `review_result.html`) для ввода и отображения
- Интеграция с NLTK
- Запуск возможен локально или через Docker

---

## 🚀 Быстрый старт

1. Установи зависимости:

```bash
pip install -r requirements.txt
python nltk_setup.py
```
2. Запусти сервер:
```bash
python manage.py runserver
```
4. Перейди в браузере:
```cpp
http://127.0.0.1:8000/
```
Вводи текст отзыва и получай результат от модели!

🐳 Запуск в Docker
```bash
docker-compose up --build
```
🗂 Структура проекта
```bash
Militans.github.io/
├── review_predictor/        # Настройки Django
├── reviews/                 # Основное приложение
├── templates/               # HTML-шаблоны
├── db.sqlite3               # SQLite база
├── Dockerfile
├── docker-compose.yml
├── nltk_setup.py
└── requirements.txt
```


🔍 Возможности
Классификация отзывов через ML-модель

Простая HTML-форма с результатом

Возможность локального запуска или через Docker

Использование Django как веб-обёртки для модели


👤 Автор
Militans
🔗 github.com/Militans

