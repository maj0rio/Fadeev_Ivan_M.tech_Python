FROM python:slim-bullseye

WORKDIR /app

RUN pip install requests filelock

COPY . .

RUN mkdir shared_resource && touch shared_resource/data.log

CMD ["python", "background_tasks.py"]
