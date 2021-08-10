FROM python:3.8.11-alpine3.14


#EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod 777 entry-point.sh
#RUN python3 app.py
ENTRYPOINT [ "./entry-point.sh" ]