import csv
import sys

"""
NOTE: We will replace this file with our own production code when grading, but you should provide your own implementations here to make sure your tests are correct.

We have provided an implementation of load_data().
"""

data = []
FILENAME = "./Data/weather_data.csv"

def load_data():
    """Loads in data from a CSV file and stores it in `data`"""
    with open(FILENAME, newline='') as datafile:
        csv_file = csv.reader(datafile)
        for row in csv_file:
            data.append(row)
    

def get_specified_column(column_heading: str) -> list[str]:
    """Retrieves all of the data in the specified column. 

    Args:
        column_heading (str): The name of the column to retrieve

    Returns:
        list[str]: A list containing all of the data from the specified column. Returns an empty list if the column does not exist.
    """
    pass

def get_data_for_date(date: str) -> list[str]:
    """Returns the weather data associated with a given date

    Args:
        date (str): The date as a string (format: "yyyy-mm-dd")

    Returns:
        list[str]: A list of strings containing all of the weather data for that date
    """   
    pass

def get_data_for_month(month: str) -> list[list]:
    """Retrieves all of the data for the specified month

    Args:
        month (str): A numeric string representing a month

    Returns:
        list[list]: A list of lists containing all of the weather data for that month
    """
    pass

def average_data_in_column(column_heading: str) -> float:
    """Finds the average of the data in a given column

    Args:
        column_heading (str): The name of the column to retrieve

    Returns:
        float: The average of all of the values in that column
    """
    pass

def main():
    load_data()
    print(data)

if __name__=='__main__':
    main()
