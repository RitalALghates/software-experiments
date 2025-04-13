# This function extracts the video ID from a YouTube URL.
# It checks the URL for different possible formats (short link, embedded, watch, etc.)
# using the 'match1' function. If no ID is found, it looks for the 'v' query parameter.
def get_vid_from_url(url):
    return match1(url, r'youtu\.be/([^?/]+)') or \
           match1(url, r'youtube\.com/embed/([^/?]+)') or \
           match1(url, r'youtube\.com/v/([^/?]+)') or \
           match1(url, r'youtube\.com/watch/([^/?]+)') or \
           parse_query_param(url, 'v') or \
           parse_query_param(parse_query_param(url, 'u'), 'v')
