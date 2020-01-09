import csv 
import os 
    
def write_csv(directory, file, line):
    """
    Writes a string to a csv file in a subdirectory where the file exists
    
    Args:
        directory (str): the name of the directory
        file (str): the name of the file
        line (list): a list to write to the file
    """
    # Make directory the file exists in
    my_path = os.path.abspath(os.path.dirname(__file__))
    directory_path = os.path.join(my_path, directory)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    csv_path = os.path.join(directory_path, file)

    mode = "w"
    if (os.path.exists(csv_path)):
        mode = "a"

    with open(csv_path, mode) as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(line)

def read_csv(file):
    """
    Read a csv file into a list 

    Args:
        file (str): the name of the file
    
    Returns:
        a list WHERE list[0] are the days and list[1] are the corresponding months
    """
    directory = "logs"

    # Make directory the file exists in
    my_path = os.path.abspath(os.path.dirname(__file__))
    directory_path = os.path.join(my_path, directory)

    if not os.path.exists(directory_path):
        print("Unable to generate graph - directory does not exist")
        return []
    
    csv_path = os.path.join(directory_path, file)

    mode = "r"
    if not os.path.exists(csv_path):
        print("Unable to generate graph - file does not exist")
        return []

    with open(csv_path, mode) as csv_file:
        lines = csv_file.readlines()

    days = []
    months = []
    for line in lines:
        data = line.split(',')
        days.append(int(data[0].strip()))
        months.append(int(data[1].strip()))

    dates = [days, months]
    return dates

def write_graph(plt, file):
    directory = "graphs"

    # Make directory the file exists in
    my_path = os.path.abspath(os.path.dirname(__file__))
    directory_path = os.path.join(my_path, directory)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    graph_path = os.path.join(directory_path, file)

    plt.savefig(graph_path)