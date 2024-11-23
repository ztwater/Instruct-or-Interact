class AccessGatewayFilter:
    def is_start_with(self, request_uri):
        prefixes = ['/api/data']
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False

