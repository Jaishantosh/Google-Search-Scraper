import requests
from bs4 import BeautifulSoup
import time

def scrape_and_format(query, num_pages):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    all_data = []
    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}"

        # Fetch the HTML content of the web page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all <a> tags with <h3> tags
        for a_tag in soup.find_all('a', href=True):
            h3_tag = a_tag.find('h3')
            if h3_tag:
                title = h3_tag.get_text(strip=True)
                link = a_tag['href']
                # Ensure the link is a full URL
                if not link.startswith("http"):
                    link = f"https://www.google.com{link}"
                all_data.append([title, link])

        # Sleep to avoid sending too many requests in a short time
        time.sleep(2)

    # Print the data in the desired format
    if all_data:
        for title, link in all_data:
            print(f"{title}\t{link}")
    else:
        print("No matching <a> tags with <h3> found.")

# site:linkedin.com/in/ ("University of Jain") AND ("india" OR "indian") AND ("student"  OR "Studying")

query = "India"

num_pages = 10  # Number of pages you want to scrape
scrape_and_format(query, num_pages)
