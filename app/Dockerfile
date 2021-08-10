FROM python:3.9.6-slim-buster


EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod 777 entry-point.sh
ENTRYPOINT [ "./entry-point.sh" ]