class URLHandler:
    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        fragment = self.url.split('#')[-1]
        return fragment