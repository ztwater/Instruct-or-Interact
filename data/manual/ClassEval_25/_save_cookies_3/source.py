class CookiesUtil:
    def _save_cookies(cookies, cookies_file):
        try:
            with open(cookies_file, 'w') as file:
                file.write(cookies)
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False