FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app app

# CMD ["gunicorn", "--conf", "app/gunicorn.conf.py", "--bind", "localhost:80", "app.app:app"]
CMD ["gunicorn", "-w 4", "--bind", "0.0.0.0:80", "app.test:app"]

# docker build -t prueba-gunicorn .
# docker container run --name gunicorn -p 80:80 prueba-gunicorn