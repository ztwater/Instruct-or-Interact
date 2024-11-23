class URLHandler:
    def get_fragment(url):
        fragment = url.split('#')[-1]
        return fragment