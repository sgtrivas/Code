import pandas as pd

def get_coordinates(csv_file):
    """
    Reads a CSV file, combines the LAT and LNG columns into coordinates formatted as
    '(LAT, LNG)', and returns them as a list.

    Parameters:
    - csv_file: str, path to the CSV file

    Returns:
    - list: A list of strings with coordinates in the format '(LAT, LNG)'
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Ensure the LAT and LNG columns exist
    if 'LAT' not in df.columns or 'LNG' not in df.columns:
        raise ValueError("The input CSV file must contain 'LAT' and 'LNG' columns.")
    
    # Combine LAT and LNG into a list of formatted strings
    coordinates = df.apply(lambda row: f"({row['LAT']}, {row['LNG']})", axis=1).tolist()
    
    return coordinates

# Example usage
coordinates = get_coordinates('Tower_dump.csv')
print(coordinates)
