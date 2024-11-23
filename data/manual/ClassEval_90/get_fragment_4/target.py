class URLHandler:
    def get_fragment(self):
        fragment = self.url.split('#')[-1]
        return fragment