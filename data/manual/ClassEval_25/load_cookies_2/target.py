class CookiesUtil:
    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        with open(self.cookies_file, 'r') as file:
            cookies_data = json.load(file)
        self.cookies = cookies_data
        return self.cookies