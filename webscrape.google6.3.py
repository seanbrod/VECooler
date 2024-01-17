from google_images_search import GoogleImagesSearch
import os
import requests
import time

def download_images(search_query, num_images=10, save_path="ws3", file_format="jpg"):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Initialize the GoogleImagesSearch object
    gis = GoogleImagesSearch("AIzaSyBESaPOQRAbiBZavSSlYkQuod9SrDuvECU", "b3b4325881eb34847")  # Replace with your actual API key and CX ID

    images_downloaded = 0
    page = 1
    downloaded_urls = set()

    # Set a custom user agent for the requests library
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    while images_downloaded < num_images:
        # Search for images
        _search_params = {
            "q": search_query,
            "num": min(num_images - images_downloaded, 100),  # API limit is 100 images per request
            "start": (page - 1) * 100,
            "fileType": file_format,
        }

        gis.search(search_params=_search_params)

        for image in gis.results():
            image_url = image.url

            if image_url in downloaded_urls:
                continue

            # Set the file extension
            if file_format == "jpg":
                file_extension = ".jpg"
            elif file_format == "png":
                file_extension = ".png"
            else:
                raise ValueError("Unsupported file format. Only 'jpg' and 'png' are supported.")

            # Create the image file name
            file_name = f"{search_query}_{images_downloaded + 1:03d}{file_extension}"
            file_path = os.path.join(save_path, file_name)

            # Download the image
            try:
                response = requests.get(image_url, headers=headers)
                response.raise_for_status()
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {file_name}")

                # Add the downloaded URL to the set to avoid duplicates
                downloaded_urls.add(image_url)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while downloading {file_name}: {e}")
                continue

            images_downloaded += 1
            if images_downloaded == num_images:
                break

            # Pause for a while before the next request
            time.sleep(2)  # Adjust the duration as needed

        page += 1

if __name__ == "__main__":
    search_query = "chip bags"
    num_images = 10
    save_path = "ws3"
    file_format = "jpg"

    download_images(search_query, num_images, save_path, file_format)
