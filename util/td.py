from datetime import datetime

from pytz import timezone

TIMEZONE_LONDON: timezone = timezone("Europe/London")
C_BERTH_STEP = "CA"       # Berth step      - description moves from "from" berth into "to", "from" berth is erased
C_BERTH_CANCEL = "CB"     # Berth cancel    - description is erased from "from" berth
C_BERTH_INTERPOSE = "CC"  # Berth interpose - description is inserted into the "to" berth, previous contents erased
C_HEARTBEAT = "CT"        # Heartbeat       - sent periodically by a train describer



{'SF_MSG': {'msg_type': 'SF', 'area_id': 'Q4', 'time': '1789998468000', 'address': '43', 'data': 'FF'}}
'body'
{'CA_MSG': {'msg_type': 'CA', 'area_id': 'Q5', 'time': '1789998469000', 'from': '0285', 'to': '0287', 'descr': '2D36'}}
'body'
{'SF_MSG': {'msg_type': 'SF', 'area_id': 'SS', 'time': '1789998470000', 'address': '59', 'data': '00'}}
'body'
{'SF_MSG': {'msg_type': 'SF', 'area_id': 'SV', 'time': '1789998471000', 'address': '03', 'data': '7F'}}
'body'
{'CA_MSG': {'msg_type': 'CA', 'area_id': 'WI', 'time': '1789998472000', 'from': '0157', 'to': '0165', 'descr': '2L43'}}
'body'


def print_td_frame(parsed):
 
    message = list(parsed.values())[0]
    message_type = message["msg_type"]

    if message_type in [C_BERTH_STEP, C_BERTH_CANCEL, C_BERTH_INTERPOSE]:
        # The feed time is in milliseconds, but python takes timestamps in seconds
        timestamp = int(message["time"]) / 1000

        area_id = message["area_id"]
        description = message.get("descr", "")
        from_berth = message.get("from", "")
        to_berth = message.get("to", "")

        utc_datetime = datetime.fromtimestamp(timestamp)
        uk_datetime = TIMEZONE_LONDON.fromutc(utc_datetime)

        print("{} [{:2}] {:2} {:4} {:>5}->{:5}".format(
            uk_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            message_type, area_id, description, from_berth, to_berth,
        ))

def extract_td_fields(parsed):
    try:
        message = list(parsed.values())[0]
        message_type = message["msg_type"]

        if message_type in [C_BERTH_STEP, C_BERTH_CANCEL, C_BERTH_INTERPOSE]:
            timestamp = int(message["time"]) / 1000

            area_id = message["area_id"]
            description = message.get("descr", "")
            from_berth = message.get("from", "")
            to_berth = message.get("to", "")

            utc_datetime = datetime.fromtimestamp(timestamp)
            uk_datetime = TIMEZONE_LONDON.fromutc(utc_datetime)
            return uk_datetime, area_id, description, from_berth, to_berth
        
    except Exception as e:
        print("Malformed message caused the following error:", e)
        return "", ""
