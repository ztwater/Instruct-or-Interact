class PageUtil:
    def search(self, keyword):
        results = []
        for item in self.data:
            if keyword in item:
                results.append(item)
        search_info = {
            "keyword": keyword,
            "total_results": len(results),
            "total_pages": (len(results) + self.page_size - 1) // self.page_size,
            "results": results
        }
        return search_info