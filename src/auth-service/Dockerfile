FROM --platform=linux/amd64 python:3.9
COPY . /auth-service
COPY requirements.txt /auth-service
WORKDIR /auth-service
RUN pip install -r requirements.txt
EXPOSE 8010
CMD ["python3", "auth-service.py"]