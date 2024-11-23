class AccessGatewayFilter:
    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        # Get the JWT token from the request headers
        jwt_token = request['headers']['Authorization']['jwt']
        
        # Verify and decode the JWT token
        try:
            decoded_token = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return None
        
        # Extract the user information from the decoded token
        user_info = decoded_token.get('user')
        
        return user_info