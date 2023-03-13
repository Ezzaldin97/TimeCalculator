from src.time_calc_engine import TimeCalculatorEngine
import pytest

def test_class_args():
        tc = TimeCalculatorEngine("3:30 PM", "2:12")
        actual = tc.added_hr
        expected = "2"
        assert(actual==expected)
def test_same_period():
        tc = TimeCalculatorEngine("3:30 PM", "2:12")
        actual = tc.add_time()
        expected = "\x1b[1;34m5:42 PM"
        assert(actual==expected)
def test_different_period():
        tc = TimeCalculatorEngine("11:55 AM", "3:12")
        actual = tc.add_time()
        expected = "\x1b[1;34m3:07 PM"
        assert(actual==expected)
def test_next_day():
        tc = TimeCalculatorEngine("9:15 PM", "5:30")
        actual = tc.add_time()
        expected = "\x1b[1;34m2:45 AM \x1b[1;32m(next day)"
        assert(actual==expected)
def test_period_change_at_twelve():
        tc = TimeCalculatorEngine("11:40 AM", "0:25")
        actual = tc.add_time()
        expected = "\x1b[1;34m12:05 PM"
        assert(actual==expected)
def test_twenty_four():
        tc = TimeCalculatorEngine("2:59 AM", "24:00")
        actual = tc.add_time()
        expected = "\x1b[1;34m2:59 AM \x1b[1;32m(next day)"
        assert(actual==expected)
def test_two_days_later():
        tc = TimeCalculatorEngine("11:59 PM", "24:05")
        actual = tc.add_time()
        expected = "\x1b[1;34m12:04 AM \x1b[31;21m(2 days later)"
        assert(actual==expected)
def test_high_duration():
        tc = TimeCalculatorEngine("8:16 PM", "466:02")
        actual = tc.add_time()
        expected = "\x1b[1;34m6:18 AM \x1b[31;21m(20 days later)"
        assert(actual==expected)
def test_two_days_later_with_day():
        tc = TimeCalculatorEngine("11:59 PM", "24:05")
        actual = tc.add_time("Wednesday")
        expected = "\x1b[1;34m12:04 AM, \x1b[33;21mFriday \x1b[31;21m(2 days later)"
        assert(actual==expected)
def test_twenty_four_with_day():
        tc = TimeCalculatorEngine("2:59 AM", "24:00")
        actual = tc.add_time(day = "saturDay")
        expected = "\x1b[1;34m2:59 AM, \x1b[33;21mSunday \x1b[1;32m(next day)"
        assert(actual==expected)
def test_not_valid_range():
        with pytest.raises(ValueError):
                tc = TimeCalculatorEngine("2:59 TM", "24:00")
                tc.add_time()
def test_not_valid_range1():
        with pytest.raises(ValueError):
                tc = TimeCalculatorEngine("2:59 AM", "24:00")
                tc.add_time("fday")
def test_not_valid_format():
        with pytest.raises(ValueError):
                tc = TimeCalculatorEngine("259 AM", "24:00")