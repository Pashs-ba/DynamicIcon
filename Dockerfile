FROM python:3.12
LABEL authors="pashs"
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]