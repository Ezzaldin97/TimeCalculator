"""
Main Module of Time Formats Validation
"""
import re
from utils.str_operations import StrOperation
from utils.colors import ColorCodes

col = ColorCodes()

class TimeFormat:
    def __init__(self, hr:str, minute:str, period:str, day:str) -> None:
        """
        init function
        parameters
        ----------
        hr:hour
        minute:minutes
        period:day period (PM,AM)
        day:day of week
        """
        self.hr = int(hr)
        self.min = int(minute)
        self.period = period
        self.day = day.lower()
    def check_time_parts(self) -> bool:
        if self.hr >= 0 and self.hr <= 12:
            if self.min >= 0 and self.min <= 60:
                if self.period in ["PM", "AM"]:
                    if self.day == "no day" or self.day in ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
                        return True
        else:
            return False
        