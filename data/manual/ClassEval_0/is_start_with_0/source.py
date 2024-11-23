class AccessGatewayFilter:
    def is_start_with(request_uri, prefixes):
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False