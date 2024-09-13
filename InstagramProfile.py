import requests
from lxml import html
import re
import sys

def main(username):
    '''Main function accepts an Instagram username and returns a dictionary object containing profile details.'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    url = f"https://www.instagram.com/{username}/?hl=en"
    page = requests.get(url, headers=headers)
    
    if page.status_code != 200:
        return {'success': False, 'message': 'Failed to retrieve the page. Status code: {}'.format(page.status_code)}
    
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[starts-with(@name,"description")]/@content')

    if data:
        # Extract description meta content
        profile_data = data[0].split(', ')
        followers = profile_data[0][:-9].strip()
        following = profile_data[1][:-9].strip()
        posts = re.findall(r'\d+[,]*', profile_data[2])[0]

        # Try to extract the user's name
        try:
            name_match = re.search(r'"name":"([^"]+)"', page.text)
            name = name_match.group(1) if name_match else 'Unknown'
        except IndexError:
            name = 'Unknown'

        # Try to extract about info (this regex might need further adjustment based on page structure)
        try:
            aboutinfo_match = re.search(r'"description":"([^"]+)"', page.text)
            aboutinfo = aboutinfo_match.group(1) if aboutinfo_match else 'No about info found'
        except IndexError:
            aboutinfo = 'No about info found'

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
    else:
        instagram_profile = {
            'success': False,
            'profile': {},
            'message': 'No profile data found.'
        }
    return instagram_profile

# python InstgramProfile.py username
if __name__ == "__main__":
    '''Driver code'''
    if len(sys.argv) == 2:
        output = main(sys.argv[-1])
        print(output)
    else:
        print('=========>Invalid parameters! The valid command is: <=========== \npython InstagramProfile.py username')
