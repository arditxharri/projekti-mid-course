FROM python:3.12

WORKDIR /app

COPY ./mirror-repos.py .

CMD ["python", "./mirror-repos.py"]
