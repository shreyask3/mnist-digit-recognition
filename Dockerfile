FROM python:3.10

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

COPY requirements.txt /app

RUN PYTHONPATH=/usr/bin/python pip install -r requirements.txt

EXPOSE 4040

CMD python app.py