import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the job search page
url = "https://www.indeed.com/jobs?q=software+engineer&l="

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract job cards
    job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')

    # Initialize lists to store the data
    job_titles = []
    company_names = []
    locations = []
    skills = []

    # Iterate over job cards to extract information
    for job_card in job_cards:
        title = job_card.find('h2', class_='title').text.strip()
        company = job_card.find('span', class_='company').text.strip()
        location = job_card.find('div', class_='recJobLoc')['data-rc-loc']

        # Attempt to extract skills or job description (where skills might be mentioned)
        description = job_card.find('div', class_='summary').text.strip()

        # Add the extracted information to the lists
        job_titles.append(title)
        company_names.append(company)
        locations.append(location)
        skills.append(description)

    # Create a DataFrame to store the scraped data
    df = pd.DataFrame({
        'Job Title': job_titles,
        'Company': company_names,
        'Location': locations,
        'Skills/Description': skills
    })

    # Display the DataFrame
    print(df)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
