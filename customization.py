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
    if 'src' in video.attrs:
        return video['src']
    if 'data-src' in video.attrs:
        return video['data-src']
    if 'data-video-url' in video.attrs:
        return video['data-video-url']
    if video.source:
        return video.source['src']
    return None
