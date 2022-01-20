def grab_video(link)->str:
    """
    This function takes a link to a video and returns the video in a string.
    :param link:
    :return:
    """
    import requests
    import re
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse

    # Get the video page
    video_page = requests.get(link)

    # Parse the page
    soup = BeautifulSoup(video_page.text, 'html.parser')
    video = soup.select_one('video')
    if video.has_attr('src'):
        return video['src']
    if video.has_attr('data-src'):
        return video['data-src']
    if video.source:
        return video.source['src']
    return None
