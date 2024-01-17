#sean Broderick

import requests
from bs4 import BeautifulSoup
import os 
import urllib

def download_images(search_query, num_images = 10, save_path ="ws2", file_format = "jpg"):
     # Create the save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Bing Images URL
    base_url = "https://www.bing.com/images/search"
    params = {"q": search_query}

    # Send an HTTP GET request
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find image elements
    image_elements = soup.select(".mimg")

    # Limit the number of images to download
    num_images = min(num_images, len(image_elements))

    for i in range(num_images):
        image_url = image_elements[i].get("src")

        # Set the file extension
        if file_format == "jpg":
            file_extension = ".jpg"
        elif file_format == "png":
            file_extension = ".png"
        else:
            raise ValueError("Unsupported file format. Only 'jpg' and 'png' are supported.")

        # Create the image file name
        file_name = f"{search_query}_{i+1:02d}{file_extension}"
        file_path = os.path.join(save_path, file_name)

        # Download the image
        urllib.request.urlretrieve(image_url, file_path)
        print(f"Downloaded {file_name}")

if __name__ == "__main__":
    # Replace 'your_search_query' with your desired search term

    search_query = "plastic clamshell containers for salads"
    num_images = 100  # Number of images to download (adjust as needed)
    save_path = "ws2"  # Directory to save the images (create this directory if not exists)
    
    file_format = "jpg"  # Change to 'png' if you want to download PNG images

    download_images(search_query, num_images, save_path, file_format)