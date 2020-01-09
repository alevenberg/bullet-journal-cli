import argparse
import datetime
from datetime import datetime
from io_generator import write_csv

parser = argparse.ArgumentParser(description='A script to track daily habits')
parser.add_argument('-w', "--write_habit",
    help="The name of the habit")
args = parser.parse_args()

DIRECTORY = "logs"

current_date = datetime.now()
year = current_date.year
filename = str(year) + "-" + args.write_habit + ".csv"

day = current_date.day
month = current_date.month
time = [day, month]

write_csv(DIRECTORY, filename, time)