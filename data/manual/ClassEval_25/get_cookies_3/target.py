class CookiesUtil:
    def get_cookies(self, response):
        """
        Gets the cookies from the specified response, and saves them to the cookies file.
        :param response: The response to get cookies from, dict.
        """
        cookies = response['cookies']
        self.cookies = cookies
    
        with open(self.cookies_file, 'w') as file:
            json.dump(cookies, file)
    
        print("Cookies saved to cookies_file.")