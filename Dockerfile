FROM continuumio/anaconda3:4.4.0
COPY . /app/
EXPOSE 4040
WORKDIR /app/
RUN pip install -r requirements.txt
CMD python app.py