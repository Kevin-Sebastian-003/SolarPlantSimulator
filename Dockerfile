FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY src/ /code/
COPY requirements.txt /code/
COPY start_server.sh /code/
RUN pip install -r requirements.txt
CMD ["./start_server.sh"]
#CMD ["sleep 20"]
