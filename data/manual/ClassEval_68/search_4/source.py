class PageUtil:
    def search(data, keyword):
        results = []
        for item in data:
            if keyword in item:
                results.append(item)
        return results