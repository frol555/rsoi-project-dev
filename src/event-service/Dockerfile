FROM --platform=linux/amd64 python:3.9
COPY . /event-service
COPY requirements.txt /event-service
WORKDIR /event-service
RUN pip install -r requirements.txt
EXPOSE 8020
CMD ["python3", "event-service.py"]