class URLHandler:
    def get_scheme(self):
        from urllib.parse import urlparse
        parsed_url = urlparse(self.url)
        return parsed_url.scheme