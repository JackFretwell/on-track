from datetime import datetime

from pytz import timezone

TIMEZONE_LONDON: timezone = timezone("Europe/London")


def print_td_frame(parsed_body):
    for outer_message in parsed_body:
        message = list(outer_message.values())[0]
        message_type = message["msg_type"]

    