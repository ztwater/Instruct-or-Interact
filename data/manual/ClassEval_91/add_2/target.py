class UrlPath:
    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')
    
        url_path.segments = ['foo', 'bar']
        """
        self.segments.append(segment)