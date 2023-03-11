import argparse
from src.time_calc_engine import TimeCalculatorEngine


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take Args to Calculate Time')
    parser.add_argument('--start', required=True, type = str, help='start time component')
    parser.add_argument('--added_time', required=True, type = str, help='Time to be Added')
    parser.add_argument('--day', required=False, type = str, help = "day of week", default="No Day")
    args = vars(parser.parse_args())
    tc = TimeCalculatorEngine(args["start"], args["added_time"])
    print(tc.add_time(args["day"]))