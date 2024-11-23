class URLHandler:
    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        # Split the URL into the base URL and the query string
        base_url, query_string = self.url.split('?')
    
        # Split the query string into individual parameters
        params = query_string.split('&')
    
        # Create a dictionary to store the parameters
        query_params = {}
    
        # Iterate over each parameter and split it into key-value pairs
        for param in params:
            key, value = param.split('=')
            query_params[key] = value
    
        # Return the dictionary of query parameters
        return query_params