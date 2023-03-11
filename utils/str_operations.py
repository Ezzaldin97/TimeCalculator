"""
Main Module for String Manipulation Used in TimeCalculator Modeule.
"""

class StrOperation:
    def __init__(self, time_component:str) -> None:
        """
        init function
        parameters
        ----------
        time_component:string time format given in this format: 12:30 PM
        """
        self.time_component = time_component
    def split_time_components(self):
        """
        split string time component into period and hour:min format
        """
        splitted_time_component = self.time_component.split(sep = " ")
        hour_format, period = splitted_time_component[0], splitted_time_component[1]
        return hour_format, period
    def split_clock_components(self, hr_format):
        """
        split string hr:min format into hour and minutes compnents
        parameters
        ----------
        hr_format:hr:min format
        """
        splitted_hr_format = hr_format.split(sep = ":")
        hours, mins=splitted_hr_format[0], splitted_hr_format[1]
        return hours, mins
    