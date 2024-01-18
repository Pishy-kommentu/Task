# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код вашего приложения в контейнер
COPY .. /app/

# Запускаем приложение
CMD ["python", "src/main.py"]
