from bs4 import BeautifulSoup
import requests
import os

def save_to_file(filename, title, company, location, stipend, published, more_info):
    """
    Writes the internship data into the specified file.

    Args:
        filename (str): The name of the file to write to.
        title (str): The title of the internship.
        company (str): The company offering the internship.
        location (str): The location of the internship.
        stipend (str): The stipend offered for the internship.
        published (str): The time when the internship was posted.
        more_info (str): A URL to more details about the internship.

    Returns:
        None
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Title : {title}\n")
        file.write(f"Company : {company}\n")
        file.write(f"Location : {location}\n")
        file.write(f"Stipend : {stipend}\n")
        file.write(f"Published : {published}\n")
        file.write(f"More Info : https://internshala.com/{more_info}\n\n\n")

# Create a directory for storing output files
if not os.path.exists('output'):
    os.makedirs('output')

# Loop to scrape data from 10 pages
for page in range(1, 11):
    print(f"Scraping Data From Page {page}\n")

    # Construct the URL for each page of internship listings
    url = f"https://internshala.com/internships/python-internship/page-{page}/"

    try:
        # Send an HTTP GET request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page {page}: {e}")
        continue  # Skip this page if there is an issue with the request
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all internship listings on the page
    internships = soup.find_all('div', class_='internship_meta')

    # Check if any internships were found
    if not internships:
        print(f"No internships found on page {page}")
        continue  # Skip to the next page if none are found

    # Loop through each internship listing
    for internship in internships:
        try:
            # Extract relevant details from each internship listing
            title = internship.find('a', class_='view_detail_button').text.strip()
            company = internship.find('a', class_='link_display_like_text view_detail_button').text.strip()
            location = internship.find('a', class_='location_link view_detail_button').text.strip()
            stipend = internship.find('span', class_='stipend').text.strip()
            published = internship.find('div', class_='status-container').text.strip()
            more_info = internship.h3.a['href']  # Extract the relative URL for more information
        except AttributeError:
            # Handle cases where an element is missing or cannot be extracted
            print(f"Failed to extract some details from an internship on page {page}")
            continue  # Skip this internship if there's an issue

        # Write internship details to the appropriate file based on when it was published
        if 'now' in published or 'hour' in published:
            save_to_file('output/Few_Hours_Ago.txt', title, company, location, stipend, published, more_info)
        elif 'day' in published:
            save_to_file('output/Few_Days_Ago.txt', title, company, location, stipend, published, more_info)
        elif 'week' in published:
            save_to_file('output/Few_Weeks_Ago.txt', title, company, location, stipend, published, more_info)

print("Scraping Done!")
