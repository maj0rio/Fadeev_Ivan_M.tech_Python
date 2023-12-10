import time
import random
from datetime import datetime, timedelta
from typing import Tuple

import requests
from filelock import FileLock


API_ENDPOINT = "http://backend:8000/api/data"
LOG_FILE_PATH = "/app/shared_resource/data.log"


# генерация случайного промежутка времени [start_time, end_time],
# на основе двух рандомно полученных значений минут,
# которые вычитаются из текущего времени
def generate_random_period() -> Tuple[datetime, datetime]:
    current_time = datetime.now()

    random_minutes_1 = random.randint(1, 1000)
    random_minutes_2 = random.randint(1, 1000)

    start_time = current_time - timedelta(minutes=random_minutes_1) - timedelta(minutes=random_minutes_2)
    end_time = current_time - timedelta(minutes=min(random_minutes_1, random_minutes_2))

    return {"start_time": start_time, "end_time": end_time}


# раз в 60 секунд ходим в наш endpoint и записываем полученные данные в файл
def fetch_and_save_data():
    try:
        response = requests.get(API_ENDPOINT, params=generate_random_period())
        data = response.json()
    except Exception as e:
        print(e)
        return

    # Firelock для обеспечения безопасного доступа к общему файлу
    # при работе с несколькими instance приложения
    lock = FileLock(LOG_FILE_PATH + ".lock")
    with lock:
        with open(LOG_FILE_PATH, "a") as log_file:
            log_file.write(str(data) + "\n")


if __name__ == "__main__":
    while True:
        fetch_and_save_data()
        time.sleep(60)
