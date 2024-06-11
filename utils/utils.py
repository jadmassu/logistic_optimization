import pandas as pd

def load_data(file1_path):
    try:
        data = pd.read_csv(file1_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return "Error loading data:", e

def merge_tables(data1, data2, common_column):
    try:
        merged_data = pd.merge(data1, data2, on=common_column)
        return merged_data
    except Exception as e:
        print("Error merging tables:", e)
        return "Error merging tables:", e

def filter_data_by_condition(data, column, condition):
    try:
        filtered_data = data[data[column] != condition]
        return filtered_data
    except Exception as e:
        print("Error filtering data:", e)
        return "Error filtering data:", e


def save_to_csv(data, output_file):
    try:
        data.to_csv(output_file, index=False)
        print("Data saved to", output_file)
        return output_file
    except Exception as e:
        print("Error saving data to CSV:", e)
        return "Error saving data to CSV:", e