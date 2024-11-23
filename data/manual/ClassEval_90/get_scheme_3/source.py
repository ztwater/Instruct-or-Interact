class URLHandler:
    def get_scheme(url):
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        return parsed_url.scheme