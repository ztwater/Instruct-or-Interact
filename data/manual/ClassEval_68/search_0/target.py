class PageUtil:
    def search(self, keyword):
        results = []
        for item in self.data:
            if keyword in item:
                results.append(item)
        search_info = {
            "keyword": keyword,
            "total_results": len(results),
            "total_pages": 1,
            "results": results
        }
        return search_info