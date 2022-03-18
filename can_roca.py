import click
import re
import time
from random import random
from datetime import date, timedelta

import requests
from dateutil.rrule import rrule, DAILY


BOOKING_LIST_URL = "https://www.covermanager.com/reservs/new_reserv_waiting"


def validate_email(ctx, param, value):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise click.BadParameter("wrong email format")

    return value


@click.command()
@click.option("--name", prompt=True, help="Put your name for the booking")
@click.option("--last_name", prompt=True, help="Put your last name for the booking")
@click.option(
    "--email",
    prompt=True,
    help="Put your mail for the booking",
    callback=validate_email,
)
@click.option("--phone", prompt=True, help="Put your phone for the booking")
@click.option("--people", prompt=True, help="Put your last name for the booking")
@click.option(
    "--restaurant",
    prompt=True,
    help="Select between restaurants",
    type=click.Choice(["celler-de-can-roca", "diverxo"], case_sensitive=False),
)
def start_booking(
    name: str, last_name: str, email: str, phone: str, people: int, restaurant: str
):
    start_dt = date.today()
    end_dt = start_dt + timedelta(days=365)

    booking_list_payload = {
        "language": "spanish",
        "hour": 3,
        "int_call_code": 34,
        "commentary_client": "",
        "food_restriction": "",
        # USER INPUT
        "restaurant": restaurant,
        "people": people,
        "user_name": name,
        "user_last_name": last_name,
        "user_email": email,
        "user_phone": phone,
    }

    for day in rrule(
        DAILY, dtstart=start_dt, until=end_dt, byweekday=[3, 4, 5]
    ):  # noqa 3 = Thursday, 4 = Friday, 5 = Saturday
        print(f'Adding to waiting list on {day.strftime("%d-%m-%Y")}')
        booking_list_payload["dia"] = day.strftime("%d-%m-%Y")
        r = requests.post(BOOKING_LIST_URL, booking_list_payload)
        print(r.content)
        time.sleep(random() * 4)


if __name__ == "__main__":
    start_booking()
