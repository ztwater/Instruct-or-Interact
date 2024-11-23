class PageUtil:
    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.search("1")
        >>> search_info = {
        >>>     "keyword": "1",
        >>>     "total_results": 1,
        >>>     "total_pages": 1,
        >>>     "results": [1]
        >>> }
        """
        results = []
        for item in self.data:
            if keyword in str(item):
                results.append(item)
        search_info = {
            "keyword": keyword,
            "total_results": len(results),
            "total_pages": (len(results) + self.page_size - 1) // self.page_size,
            "results": results
        }
        return search_info