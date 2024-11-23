class AccessGatewayFilter:
    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True
        """
        prefixes = ['/api/']  # Add the desired prefixes here
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False
