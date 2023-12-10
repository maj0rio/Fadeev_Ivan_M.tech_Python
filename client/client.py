import os
import random
import requests

import asyncio
from retry import retry


N_THREADS = int(os.getenv('N_THREADS'))
MAX_DELAY = int(os.getenv('MAX_DELAY'))
LOG_FILE = 'log.txt'

possible_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
possible_uris = [
    "/api/users", "/api/posts", "/api/comments",
    "/api/products", "api/data", "api/pages", "api/auth",
    "/api/login", "api/docs"
]
possible_status_codes = [
    "200", "201", "204",
    "400", "401", "403", "404",
    "500"
]


# генерируем здесь случайный ip адрес, состоящий из 4 чисел от 0 до 255
def generate_ip_address() -> str:
    return '.'.join([str(random.randint(0, 255)) for i in range(4)])


def write_in_file(log_text) -> None:
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_text + "\n")


# декоратор reply нужен для того что, контейнер backend успел запуститься и
# начал нормально не работать, без декоратора пришлось два раза запускать docker-compose
@retry(exceptions=requests.exceptions.ConnectionError, delay=5, backoff=5, max_delay=15)
def send_request() -> None:
    ip_address = generate_ip_address()
    http_method = random.choice(possible_methods)
    uri = random.choice(possible_uris)
    http_status_code = random.choice(possible_status_codes)
    log_text = f"{ip_address} {http_method} {uri} {http_status_code}"
    write_in_file(log_text)

    response = requests.post(
        "http://backend:8000/api/data",
        json={"log": log_text}
    )


async def worker() -> None:
    while True:
        send_request()
        await asyncio.sleep(random.randint(0, MAX_DELAY))


async def main() -> None:
    tasks = [worker() for _ in range(N_THREADS)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
