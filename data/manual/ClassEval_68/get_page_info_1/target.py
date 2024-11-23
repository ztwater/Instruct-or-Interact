class PageUtil:
    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        current_page = page_number
        per_page = self.page_size
        total_pages = self.total_pages
        total_items = self.total_items
        has_previous = page_number > 1
        has_next = page_number < total_pages
        start_index = (page_number - 1) * per_page
        end_index = min(start_index + per_page, total_items)
        data = self.data[start_index:end_index]
        
        return {
            "current_page": current_page,
            "per_page": per_page,
            "total_pages": total_pages,
            "total_items": total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }