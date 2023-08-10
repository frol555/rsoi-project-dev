FROM --platform=linux/amd64 python:3.9
COPY . /pay-service
COPY requirements.txt /pay-service
WORKDIR /pay-service
RUN pip install -r requirements.txt
EXPOSE 8040
CMD ["python3", "pay-service.py"]