# Time Calculator Project

## Description:
Project for Calculating Time after Adding (Hours, Minutes) to Initial Time.

### example:
Initial Time: 12:30 PM
Added Time: 24:00
Final Result : 12:30 PM (next day)

## Usage:

### Installation:
`` pip install -r requirements.txt ``

### Running:
The Project runs with the following command
`` python main.py --start {ex:12:30 PM} --added_time {ex:24:00} --day{optional, ex:friday}``
running command parameter:
- start: start time
- added_time: time to be added
- day: start day of the week

### Testing:
Tests could be launched be the command ``pytest test_time_calc.py``,
all tests inside test_time_calc.py.