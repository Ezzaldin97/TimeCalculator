
class TimeFormat:
    def __init__(self, hr:str, minute:str, period:str) -> None:
        self.hr = int(hr)
        self.min = int(minute)
        self.period = period
    def check_time_parts(self) -> bool:
        if self.hr >= 0 and self.hr <= 12:
            if self.min >= 0 and self.min <= 60:
                if self.period in ["PM", "AM"]:
                    return True
        else:
            return False
        