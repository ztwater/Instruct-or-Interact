class URLHandler:
    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        """
        from urllib.parse import urlparse
        parsed_url = urlparse(self.url)
        return parsed_url.scheme