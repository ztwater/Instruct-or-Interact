class CookiesUtil:
    def get_cookies(self, response):
        """
        Gets the cookies from the specified response, and saves it to cookies_file.
        :param response: The response to get cookies from, dict.
        """
        cookies = response['cookies']
        
        with open(self.cookies_file, 'w') as file:
            for key, value in cookies.items():
                file.write(f"{key}={value}\n")
        
        self.load_cookies()
        print("Cookies saved to cookies_file.")