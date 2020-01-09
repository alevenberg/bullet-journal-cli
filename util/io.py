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

    # Check if line already written
    
    with open(csv_path, mode) as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(line)

def read_csv():