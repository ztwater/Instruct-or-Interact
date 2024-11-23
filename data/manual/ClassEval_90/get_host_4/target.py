class URLHandler:
    def get_host(self):
        # Remove the protocol part of the URL
        url = self.url.replace("http://", "").replace("https://", "")
        
        # Split the URL by "/"
        parts = url.split("/")
        
        # Return the second part of the URL, which is the host domain name
        return parts[1]