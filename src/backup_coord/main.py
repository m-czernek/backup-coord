import sys
import requests
import os
import logging

from datetime import datetime
from requests.exceptions import RequestException

MONTH_COORD_MAPPING: dict[int, str] = {
    1: "Victor Zhestkov",
    2: "Yeray Gutiérrez",
    3: "Marek Czernek",
    4: "Alex Graul",
    5: "Yeray Gutiérrez",
    6: "Marek Czernek",
    7: "Marek Czernek",
    8: "Victor Zhestkov",
    9: "Alex Graul",
    10: "Yeray Gutiérrez",
    11: "Victor Zhestkov",
    12: "Alex Graul",
}
URL_ENV_KEY = "slack_webhook_url"

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

def select_person() -> str:
    month = datetime.now().month
    person = MONTH_COORD_MAPPING.get(month)
    if not person:
        raise ValueError(f"Unknown mapping for {month}. month in {MONTH_COORD_MAPPING}")
    return person

def trigger_workflow(backup_coord: str):
    payload = {"person": backup_coord}
    url = os.environ.get(URL_ENV_KEY)
    if not url:
        raise ValueError(f"Payload URL not set; set the {URL_ENV_KEY} property with the Slack workflow webhook")
    try:
        log.info(f"Sending POST to {url} with {payload} payload")
        res = requests.post(url, json=payload)
        log.info(res.text)
    except RequestException as e:
        log.error("Failed to trigger Slack flow")
        log.error(e)

def main():
    trigger_workflow(select_person())

if __name__ == "__main__":
    main()