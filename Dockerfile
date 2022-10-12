FROM python:3.10.7-slim-buster

WORKDIR /app

COPY app.py .

COPY model_gbr.pkl .

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]