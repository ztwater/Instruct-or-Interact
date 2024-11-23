class AccessGatewayFilter:
    def set_current_user_info_and_log(self, user):
        # Set the current user information
        current_user_info = user

        # Log the access
        log_message = f"Access logged for user: {current_user_info}"
        print(log_message)