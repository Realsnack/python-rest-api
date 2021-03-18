FROM python:3.6

COPY ./src /src
RUN pip install -r /app/requirements.txt

EXPOSE 5050
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5050"]