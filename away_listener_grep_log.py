from datetime import datetime
from enum import Enum
from typing import Tuple, Mapping

LOG_PATH = "/Users/fung.mak/dev/bee/clicker/log/away_listener.log"

Records = Mapping[str, list[datetime, datetime]]


class LOG_TYPE(Enum):
    RESUME = "resume"
    IDLE = "idle"


def read_log(log: str) -> Tuple[str, datetime, LOG_TYPE]:
    l_date, l_time, _, _, _, _, _, _, l_type = log.split(" ")
    l_datetime = datetime.strptime("{} {}".format(l_date, l_time), '%Y-%m-%d %H:%M:%S')
    l_type = l_type.replace("\n", "")
    return l_date, l_datetime, l_type


def read_file_log(log_path: str) -> Records:
    with open(log_path) as f:
        records: Mapping[str, list[datetime, datetime]] = {}
        lines = f.readlines()
        for x in lines:
            date, l_datetime, l_type = read_log(x)
            record = [None, None]
            if date in records:
                record = records[date]
            l_start, l_end = record[0], record[1]
            if l_type == LOG_TYPE.RESUME.value and l_start is None:
                record = [l_datetime, l_end]
            elif l_type == LOG_TYPE.IDLE.value:
                record = [l_start, l_datetime]
            records[date] = record
        return records


def start():
    records = read_file_log(LOG_PATH)
    for k in records:
        l_start, l_end = records[k]
        print("{} | start: {} | end: {}".format(k, l_start, l_end))


if __name__ == '__main__':
    start()
