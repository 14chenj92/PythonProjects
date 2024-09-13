from tqdm import tqdm
import requests
import re
from PIL import Image

def pp_download(username):
    url = f"https://www.instagram.com/{username}/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    try:
        # Fetch the profile page
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve page for {username}, status code: {response.status_code}")
            return
        
        # Debug: print part of the response content to inspect the HTML structure
        print("Page content preview:")
        print(response.text[:2000])  # Print the first 2000 characters for inspection

        # Search for the profile picture URL using a more general regex pattern
        match = re.search(r'"profile_pic_url_hd":"(http[^"]+)"', response.text)
        if not match:
            print("Could not find the profile picture URL in the page source.")
            return
        
        # Extract the URL and clean it up
        pp_url = match.group(1).replace("\\u0026", "&")  # Handle escaped characters in the URL
        print(f"Profile picture URL: {pp_url}")

        # Download the image
        file_size_request = requests.get(pp_url, stream=True)
        file_size = int(file_size_request.headers.get('Content-Length', 0))
        block_size = 1024  # 1 KB blocks for progress bar
        
        # Use tqdm to display the download progress
        t = tqdm(total=file_size, unit='B', unit_scale=True, desc=username, ascii=True)
        with open(username + '.jpg', 'wb') as f:
            for data in file_size_request.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

        # Show the downloaded image
        im = Image.open(username + ".jpg")
        im.show()
        print(f"Profile picture downloaded successfully as {username}.jpg")

    except Exception as e:
        print(f"An error occurred: {e}")


pp_download('stephencurry30')
