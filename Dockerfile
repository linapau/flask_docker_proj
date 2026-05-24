FROM python:3.14.2-slim

# Python runtime
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# working directory in container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# start aplikacji
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]