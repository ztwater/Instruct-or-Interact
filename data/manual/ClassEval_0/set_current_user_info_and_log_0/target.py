class AccessGatewayFilter:
    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """

        # Set the current user information
        self.current_user_info = user

        # Log the access
        log_message = f"Access logged for user: {self.current_user_info}"
        logging.info(log_message)