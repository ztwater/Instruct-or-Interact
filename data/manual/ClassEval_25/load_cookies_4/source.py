class CookiesUtil:
    def load_cookies(cookies_file):
        with open(cookies_file, 'r') as file:
            cookies_data = file.read()
        return cookies_data