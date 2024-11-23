class CookiesUtil:
    def get_cookies(url, cookies_file):
        response = requests.get(url)
        cookies = response.cookies
    
        with open(cookies_file, 'w') as file:
            for cookie in cookies:
                file.write(f"{cookie.name}={cookie.value}\n")
    
        print("Cookies saved to cookies_file.")
    