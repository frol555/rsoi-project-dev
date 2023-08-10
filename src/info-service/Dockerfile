FROM --platform=linux/amd64 python:3.9
COPY . /info-service
COPY requirements.txt /info-service
WORKDIR /info-service
RUN pip install -r requirements.txt
EXPOSE 8030
CMD ["python3", "info-service.py"]