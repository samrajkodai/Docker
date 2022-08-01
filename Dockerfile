FROM python:3.8
WORKDIR /app
RUN pip install requests
COPY . /app

CMD ["python","code.py"]