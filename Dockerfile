FROM python:3.6

COPY ./src /src
WORKDIR /src
RUN pip install -r /src/requirements.txt

EXPOSE 5050
CMD ["python3", "start.py"]