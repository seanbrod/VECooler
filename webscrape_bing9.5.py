#sean Broderick
#Bing Images Webscraper Version: 9.5
#7/19/2023

import requests
from bs4 import BeautifulSoup
import os
import time

def is_valid_image_url(image_url):
    try:
        response = requests.head(image_url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def download_images(search_query, num_images=10, save_path="ws3", file_format="jpg"): #save path must be changed
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Bing Images URL
    base_url = "https://www.bing.com/images/search"
    params = {"q": search_query, "first": 0}  # Added "first" parameter to start from the first page

    # Create a session and set headers
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    }

    images_downloaded = 0
    page = 0

    while images_downloaded < num_images:
        try:
            # Send an HTTP GET request with headers
            response = session.get(base_url, params=params, headers=headers)
            response.raise_for_status()

            # Parse the response content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find image elements
            image_elements = soup.select(".mimg")

            # Check if there are no more images to download
            if not image_elements:
                print("No more images to download.")
                break

            for i, image_element in enumerate(image_elements):
                image_url = image_element.get("src") or image_element.get("data-src") # tries src seletor and if invalid it skips and comes back with data-src selector
                if not image_url or not is_valid_image_url(image_url):
                    print(f"Image URL not found or invalid for image {i+1}. Skipping...")
                    continue

                # Set the file extension
                if file_format == "jpg":
                    file_extension = ".jpg"
                elif file_format == "png":
                    file_extension = ".png"
                else:
                    raise ValueError("Unsupported file format. Only 'jpg' and 'png' are supported.")

                # Create the image file name
                file_name = f"{search_query}_{images_downloaded + 1:02d}{file_extension}"
                file_path = os.path.join(save_path, file_name)

                # Download the image
                response = requests.get(image_url)
                response.raise_for_status()
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {file_name}")

                images_downloaded += 1
                if images_downloaded == num_images:
                    break

                # Pause for a while before the next request
                time.sleep(2)  # Adjust the duration as needed

            # Move to the next page
            page += 1
            params["first"] = page * 35  # Bing shows 35 images per page

        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    search_query = "bags of chips" #Query Change *
    num_images = 200 #Num Change *
    save_path = "ws3" #Path Change *
    file_format = "jpg"

    download_images(search_query, num_images, save_path, file_format)
