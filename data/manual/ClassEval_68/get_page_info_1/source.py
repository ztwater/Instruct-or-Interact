class PageUtil:
    def get_page_info(page_url):
        # Retrieve information about the page using the provided URL
        # You can use libraries like requests or BeautifulSoup to make HTTP requests and parse HTML
        
        # Example code using requests and BeautifulSoup:
        import requests
        from bs4 import BeautifulSoup
        
        # Make a GET request to the page URL
        response = requests.get(page_url)
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Retrieve specific information from the page
        # Example: Get the page title
        page_title = soup.title.text
        
        # Example: Get the number of links on the page
        links = soup.find_all('a')
        num_links = len(links)
        
        # Return the retrieved information
        return {
            'title': page_title,
            'num_links': num_links
        }