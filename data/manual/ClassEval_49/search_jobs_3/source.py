class JobMarketplace:
    def search_jobs(requirements):
        positions = [
            {"title": "Software Engineer", "location": "New York", "salary": 100000},
            {"title": "Data Analyst", "location": "San Francisco", "salary": 90000},
            {"title": "Product Manager", "location": "Seattle", "salary": 110000},
            {"title": "UX Designer", "location": "Los Angeles", "salary": 95000}
        ]
        
        matching_positions = []
        
        for position in positions:
            if all(req in position.values() for req in requirements):
                matching_positions.append(position)
        
        return matching_positions