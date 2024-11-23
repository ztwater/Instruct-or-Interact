class URLHandler:
    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        # Remove the protocol part of the URL
        url = self.url.replace("http://", "").replace("https://", "")
        
        # Split the URL by "/"
        parts = url.split("/")
        
        # Return the second part of the URL, which is the host domain name
        return parts[1]