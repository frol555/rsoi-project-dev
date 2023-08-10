FROM --platform=linux/amd64 python:3.9
COPY . /statistic-service
COPY requirements.txt /statistic-service
WORKDIR /statistic-service
RUN pip install -r requirements.txt
EXPOSE 8050
CMD ["python3", "statistic-service.py"]