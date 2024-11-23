class AccessGatewayFilter:
    def is_start_with(self, request_uri):
        prefixes = ['/api/data']  # Add the prefixes to check against
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False