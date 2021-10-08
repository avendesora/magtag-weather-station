from typing import List

from src.helpers import format_time
from tests.conftest import TestTime


def test_format_time(times: List[TestTime]):
    for test_time in times:
        assert format_time(test_time.time_struct, True) == test_time.twelve_hour_time
        assert format_time(test_time.time_struct, False) == test_time.twenty_four_hour_time
