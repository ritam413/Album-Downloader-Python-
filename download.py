import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Function to download images from a URL
def download_images(url, folder_name='downloaded_images'):
    # Ensure the custom folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error fetching the webpage: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    for img in img_tags:
        # Get the image source URL
        img_url = img.get('src')
        if not img_url:
            continue

        # Handle relative URLs
        img_url = urljoin(url, img_url)

        # Get the image file name
        img_name = os.path.basename(img_url)

        # Download the image
        try:
            img_response = requests.get(img_url)
            with open(os.path.join(folder_name, img_name), 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")


# Example usage
website_url = 'https://example.com'  # Replace with the website URL
custom_folder_path = 'C:/Downloads'# Specify your desired folder path here

website_url2 = 'https://example.com'  # Replace with the website URL
custom_folder_path2 = 'C:/Downloads'# Specify your desired folder path here
# To Download Multiple files from multiple link Just keep on adding this two variavle   "website_url{here update the number}" and "custom_folder_path{here give the update the numver to create a new variable}"  


#TO  download more than two files just call the download_images() function with the new varaible name 
download_images(website_url, custom_folder_path)
download_images(website_url2, custom_folder_path2)