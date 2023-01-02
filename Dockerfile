FROM python:3.6
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN PYTHONPATH=/usr/bin/python pip install -r requirements.txt
EXPOSE 4040
CMD python app.py
