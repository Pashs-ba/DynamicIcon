import datetime
import os
import typing

import yaml


def load_config() -> dict:
    return yaml.safe_load(open(f"{os.path.dirname(__file__)}/config.yaml"))


def get_img_list(config: dict) -> typing.List[str]:
    images = os.listdir(config["base"]["img_folder"])
    return list(map(lambda path: os.path.join(config["base"]["img_folder"], path), images))


def get_current_slot(current_hour: int, time_slots: int):
    for i in range(1, time_slots):
        left_border = (i - 1) * (24 // time_slots)
        right_border = i * (24 // time_slots)
        if left_border <= current_hour < right_border:
            return i - 1
    return time_slots - 1


def get_current_image(config: dict) -> str:
    images = sorted(get_img_list(config))
    time_slots = 24 // len(images)
    current_hour = datetime.datetime.now().hour+3
    return images[get_current_slot(current_hour, time_slots)]


def log(config: dict, message: str):
    with open(config["other"]["logfile"], "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")


if __name__ == '__main__':
    print(get_current_image(load_config()))
