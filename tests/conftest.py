from dataclasses import dataclass

import pytest


@dataclass
class TimeStruct:
    tm_hour: int
    tm_min: int


@dataclass
class TestTime:
    time_struct: TimeStruct
    twelve_hour_time: str
    twenty_four_hour_time: str


@pytest.fixture
def times():
    return [
        TestTime(TimeStruct(0, 0), "12:00am", "00:00"),
        TestTime(TimeStruct(1, 10), "01:10am", "01:10"),
        TestTime(TimeStruct(2, 20), "02:20am", "02:20"),
        TestTime(TimeStruct(11, 30), "11:30am", "11:30"),
        TestTime(TimeStruct(12, 0), "12:00pm", "12:00"),
        TestTime(TimeStruct(13, 0), "01:00pm", "13:00"),
        TestTime(TimeStruct(23, 59), "11:59pm", "23:59"),
    ]
