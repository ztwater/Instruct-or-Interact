class URLHandler:
    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        parts = self.url.split('/')
        if len(parts) >= 3:
            return "/" + "/".join(parts[3:])
        else:
            return None
