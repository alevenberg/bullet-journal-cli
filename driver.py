import argparse
from datetime import datetime 
import sys 
from calendar_grapher import plot_calendar_year
from io_generator import read_csv
from io_generator import write_graph

# Argument Parsing
parser = argparse.ArgumentParser(description='A script to track daily habits')
parser.add_argument('-g', "--graph_habit",
    help="The name of the habit")
args = parser.parse_args()

current_date = datetime.now()
year = current_date.year
filename = str(year) + "-" + args.graph_habit
csv_file = filename + ".csv"

# Read from log
dates = read_csv(csv_file)

if len(dates) != 2:
    print ("Unable to read csv")
    sys.exit()
days = dates[0]
months = dates[1]

plt = plot_calendar_year(days, months)
plt.title(args.graph_habit + " in " + str(year))

graph_file = filename + ".png"

write_graph(plt, graph_file)
