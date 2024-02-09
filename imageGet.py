import requests

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved at: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")