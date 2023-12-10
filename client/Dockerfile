FROM python:slim-bullseye

WORKDIR /client

RUN pip install asyncio requests retry

RUN touch log.txt

COPY . .

CMD ["python", "client.py"]
