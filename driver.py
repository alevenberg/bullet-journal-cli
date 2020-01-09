from util.calendar_grapher import plot_calendar_year
from util.io import read_csv

# Argument Parsing
parser = argparse.ArgumentParser(description='A script to track daily habits')
parser.add_argument('-w', "--write_habit",
    help="The name of the habit")
args = parser.parse_args()

# Read from log
full_moon_day = [2, 2, 2, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22]
full_moon_month = [1, 1, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Generate plot
plot_calendar_year(full_moon_day, full_moon_month)