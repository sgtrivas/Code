import folium
import pandas as pd

def plot_route_on_map(locations):
    """Plots a route on a Folium map.

    Args:
        locations: A list of tuples representing latitude and longitude coordinates.
    """

    if not locations:
        return None

    # Create a Folium map centered on the first location
    map_center = locations[0]
    my_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each location
    for loc in locations:
        folium.Marker(loc).add_to(my_map)

    # Draw a line connecting the locations
    folium.PolyLine(locations, color="blue", weight=2.5, opacity=1).add_to(my_map)

    return my_map

def get_coordinates(csv_file):
    """
    Reads a CSV file, combines the LAT and LNG columns into a list of tuples,
    and returns them.

    Parameters:
    - csv_file: str, path to the CSV file

    Returns:
    - list: A list of tuples with coordinates in the format (LAT, LNG)
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Ensure the LAT and LNG columns exist
    if 'LAT' not in df.columns or 'LNG' not in df.columns:
        raise ValueError("The input CSV file must contain 'LAT' and 'LNG' columns.")
    
    # Combine LAT and LNG into a list of tuples
    coordinates = df.apply(lambda row: (row['LAT'], row['LNG']), axis=1).tolist()
    
    return coordinates

# Example usage
csv_file = 'Bluetooth_dump.csv'  # Replace with your file path
coordinates = get_coordinates(csv_file)
my_map = plot_route_on_map(coordinates)

# Save the map to an HTML file
my_map.save("Bluetooth_dump.html")
