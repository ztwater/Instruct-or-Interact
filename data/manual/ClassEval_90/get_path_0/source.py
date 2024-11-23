class URLHandler:
    def get_path(url):
        parts = url.split('/')
        if len(parts) >= 3:
            return parts[2]
        else:
            return None