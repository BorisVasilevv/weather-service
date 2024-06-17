# Используем официальный образ Python в качестве основы
FROM python:3.10

# Установим рабочую директорию в контейнере
WORKDIR /app

# Скопируем зависимости проекта в контейнер
COPY requirements.txt .

# Установим зависимости
RUN pip install -r requirements.txt

# Скопируем все файлы проекта в контейнер
COPY . .

# Команда для запуска приложения
CMD ["python", "weatherService.py"]

# Откроем порт для внешних подключений
EXPOSE 7777

# docker build -t weatherService .
# docker run -p 7777:7777 --name weatherService weatherService