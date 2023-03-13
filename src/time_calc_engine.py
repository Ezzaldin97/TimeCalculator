"""
Main Module for Time Calculator Engine
"""
from utils.str_operations import StrOperation
from utils.colors import ColorCodes
from utils.check_time_format import TimeFormat
import re

col = ColorCodes()

class TimeCalculatorEngine:
    def __init__(self, time_component:str, added_time:str) -> None:
        """
        init function
        parameters
        ----------
        time_component:string time format given in this format: 12:30 PM
        added_time: hours:mins: 30:09
        """
        if re.search(r"\d{1,2}\:{1}\d{1,2}\s{0,1}[PMA]{0,2}", time_component) and re.search(r"\d{1,2}\:{1}\d{1,2}\s{0,1}[PMA]{0,2}", added_time):
            strOps = StrOperation(time_component)
            self.time_component = time_component
            self.added_time = added_time
            self.clock_format, self.period = strOps.split_time_components()
            self.period = self.period.upper()
            self.hr_time_component, self.min_time_component = strOps.split_clock_components(self.clock_format)
            self.added_hr, self.added_min = strOps.split_clock_components(added_time)
        else:
            raise ValueError(f"{col.red}Time Format is not correct\nformat must be [hour]:[minute] [period]")
    @staticmethod
    def _calc_minutes(min_time_component:str, added_min:str):
        increased_hr, total_mins=0, None
        total=int(added_min)+int(min_time_component)
        if total<60:
            total_mins=total
            return increased_hr, total_mins
        elif total>60:
            total_mins=total-60
            increased_hr+=1
            return increased_hr, total_mins
        else:
            total_mins=0
            increased_hr+=1
            return increased_hr, total_mins
    @staticmethod
    def _calc_hr(period:str, hr_time_component:str, added_hr:str):
        initial_period, initial_hr, counter=period, int(hr_time_component), 0
        for i in range(0,int(added_hr)):
            initial_hr+=1
            if initial_hr>12:
                initial_hr=1
                if initial_period=='PM':
                    initial_period='AM'
                    counter+=1
                else:
                    initial_period='PM'
        return initial_period, initial_hr, counter
    @staticmethod
    def _calc_time(hr_increased:int, total_mins:int, period:str, hr:int, num_days:int):
        current_hr = hr + hr_increased
        if current_hr>12:
            current_hr=1
            if period=='AM':
                period='PM'
            else:
                period='AM'
                num_days+=1
        elif current_hr==12:
            if period=='PM':
                if total_mins>0:
                    period='AM'
                    num_days+=1
            else:
                if total_mins>0:
                    period='PM'
        return current_hr, total_mins, period, num_days
    @staticmethod
    def _current_day(day:str, num_days:int) -> str:
        if day !='No Day':
            day=day.lower()
            for i in range(num_days):
                if day=='saturday':
                    day='sunday'
                elif  day=='sunday':
                    day='monday'
                elif day=='monday':
                    day='tuesday'
                elif day=='tuesday':
                    day='wednesday'
                elif day=='wednesday':
                    day='thursday'
                elif day=='thursday':
                    day='friday'
                elif day=='friday':
                    day='saturday'
        return day
    def add_time(self, day:str="No Day") -> str:
        """
        calculate time interval and produce it as string after adding the duration
        parameters
        ----------
        day:Day of Week
        """
        tf = TimeFormat(self.hr_time_component, self.min_time_component, self.period, day)
        if tf.check_time_parts():
            increased_hr, total_mins = TimeCalculatorEngine._calc_minutes(self.min_time_component, self.added_min)
            initial_period, initial_hr, counter = TimeCalculatorEngine._calc_hr(self.period, self.hr_time_component, self.added_hr)
            current_hr, final_total_mins, period, num_days = TimeCalculatorEngine._calc_time(increased_hr, total_mins, initial_period, initial_hr, counter)
            day = TimeCalculatorEngine._current_day(day, num_days)
            final_total_mins_str = f"{final_total_mins:02}"
            if day=='No Day':
                if num_days==0:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period}"
                elif num_days==1:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period} {col.green}(next day)"
                else:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period} {col.red}({str(num_days)} days later)"
            else:
                day=day.capitalize()
                if num_days==0:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period}, {col.yellow}{day}"
                elif num_days==1:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period}, {col.yellow}{day} {col.green}(next day)"
                else:
                    return f"{col.blue}{str(current_hr)}:{final_total_mins_str} {period}, {col.yellow}{day} {col.red}({str(num_days)} days later)"
        else:
            raise ValueError(f"{col.red}Hour, Minute, Period or Day is outside the Valid Range")