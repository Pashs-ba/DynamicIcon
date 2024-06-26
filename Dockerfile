FROM python:alpine:3.12
LABEL authors="pashs"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]