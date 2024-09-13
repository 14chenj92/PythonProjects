import requests
from lxml import html
import re
import sys
import pprint
from profilepic import pp_download

def banner():
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('\t                         Instagram Profile Data Grabber                    ')
    print('\t""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')


def main(username):
    '''Main function accepts Instagram username and returns a dictionary containing profile details.'''
    banner()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    url = f"https://www.instagram.com/{username}/?hl=en"
    
    # Make the request
    page = requests.get(url, headers=headers)
    
    # Handle potential page errors
    if page.status_code != 200:
        print(f"Failed to retrieve page for {username}, status code: {page.status_code}")
        return {'success': False, 'profile': {}, 'message': 'Page request failed'}

    # Parse the page content
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[starts-with(@name,"description")]/@content')

    if data:
        try:
            # Extract profile info from the description meta tag
            profile_data = data[0].split(', ')
            followers = profile_data[0][:-9].strip()
            following = profile_data[1][:-9].strip()
            posts = re.findall(r'\d+[,]*', profile_data[2])[0]

            # Try to extract the user's name
            name_match = re.search(r'"name":"([^"]+)"', page.text)
            name = name_match.group(1) if name_match else 'Unknown'

            # Try to extract about info
            aboutinfo_match = re.search(r'"description":"([^"]+)"', page.text)
            aboutinfo = aboutinfo_match.group(1) if aboutinfo_match else 'No about info found'

            # Prepare the final result
            instagram_profile = {
                'success': True,
                'profile': {
                    'name': name,
                    'profileurl': url,
                    'username': username,
                    'followers': followers,
                    'following': following,
                    'posts': posts,
                    'aboutinfo': aboutinfo
                }
            }

        except (IndexError, AttributeError) as e:
            print(f"Error parsing profile data: {e}")
            instagram_profile = {'success': False, 'profile': {}, 'message': 'Parsing error'}
    else:
        instagram_profile = {
            'success': False,
            'profile': {},
            'message': 'No profile data found'
        }

    return instagram_profile


#  Usage: python main.py username
if __name__ == "__main__":

    if len(sys.argv) == 2:
        username = sys.argv[-1]

        # Fetch the Instagram profile data
        output = main(username)

        # Download the profile picture
        pp_download(username)

        # Print the profile data
        pprint.pprint(output)

    else:
        print('Invalid parameters. Usage: python main.py <username>')
