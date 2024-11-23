class CookiesUtil:
    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """
        try:
            with open(self.cookies_file, 'w') as file:
                file.write(json.dumps(self.cookies))
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False