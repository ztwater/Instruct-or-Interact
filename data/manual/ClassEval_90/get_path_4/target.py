class URLHandler:
    def get_path(self):
        parts = self.url.split('/')
        if len(parts) >= 3:
            return '/' + '/'.join(parts[3:])
        else:
            return None