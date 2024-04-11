import requests
from bs4 import BeautifulSoup
def get_hyperlinks(url):
  """Fetches the HTML content of a website and extracts all hyperlinks.

  Args:
      url: The URL of the website to scrape.

  Returns:
      A list of strings containing the hyperlinks found on the website.
  """

  # Send an HTTP GET request to fetch the HTML content
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)

    # Find all anchor tags (<a>) containing hyperlinks
    links = soup.find_all('a')
    #print(links)
    # Extract the 'href' attribute containing the hyperlink URL
    hyperlinks = [link.get('href') for link in links if link.get('href')]
    #print(str(hyperlinks).replace('/en/channels/', ''))
    return hyperlinks
  else:
    print(f"Error: Failed to retrieve webpage from {url}")
    return []

# Example usage
target_url = "https://telemetr.io/en/channels"  # Replace with the target website URL
hyperlinks = get_hyperlinks(target_url)

# Print the extracted hyperlinks
if hyperlinks:
  print("Hyperlinks on", target_url)
  for link in hyperlinks:
    print(target_url+str(link).replace('/en/channels', '').replace('/en/category','').replace('/en/pricing','').replace('/en/country',''))
else:
  print("No hyperlinks found on", target_url)