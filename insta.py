from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import sys
import pprint

def banner():
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('\t                         Instagram Profile Data Grabber                    ')
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

def fetch_profile_info(username):
    '''Fetch Instagram profile info using Selenium'''
    banner()

    # Setup ChromeDriver using webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = f"https://www.instagram.com/{username}/?hl=en"
    driver.get(url)
    
    profile_info = {
        'name': 'Unknown',
        'profileurl': url,
        'username': username,
        'followers': 'Unknown',
        'following': 'Unknown',
        'posts': 'Unknown',
        'aboutinfo': 'No about info found'
    }

    try:
        # Wait for the page to load
        driver.implicitly_wait(10)
        
        # Get page source
        page_source = driver.page_source

        # Extract profile data from page source
        description_meta = re.search(r'<meta name="description" content="([^"]+)"', page_source)
        if description_meta:
            data = description_meta.group(1).split(', ')
            profile_info['followers'] = data[0][:-9].strip()
            profile_info['following'] = data[1][:-9].strip()
            profile_info['posts'] = re.findall(r'\d+[,]*', data[2])[0]
        
        # Extract user's name
        name_match = re.search(r'"name":"([^"]+)"', page_source)
        profile_info['name'] = name_match.group(1) if name_match else 'Unknown'
        
        # Extract about info
        aboutinfo_match = re.search(r'"description":"([^"]+)"', page_source)
        profile_info['aboutinfo'] = aboutinfo_match.group(1) if aboutinfo_match else 'No about info found'
        
    except Exception as e:
        print(f"Error fetching profile info: {e}")
    
    finally:
        driver.quit()
    
    return profile_info

# Usage: python script_name.py username
if __name__ == "__main__":
    if len(sys.argv) == 2:
        username = sys.argv[-1]
        profile_data = fetch_profile_info(username)
        pprint.pprint(profile_data)
    else:
        print('Invalid parameters. Usage: python script_name.py <username>')
