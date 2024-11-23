class AccessGatewayFilter:
    def get_jwt_user(self, request):
        # Get the JWT token from the request headers or cookies
        jwt_token = request['headers'].get('Authorization')
    
        # Verify and decode the JWT token
        try:
            decoded_token = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return None
    
        # Extract the user information from the decoded token
        user_info = decoded_token.get('user')
    
        return user_info