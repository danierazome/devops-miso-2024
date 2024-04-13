FROM python:3.9

WORKDIR /app

COPY config.py models.py routes.py app.py requirements.txt /app/
COPY migrations /app/migrations

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["python", "/app/app.py"]
