class XMLProcessor:
    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file.
        """
        tree = ET.parse(self.file_name)
        self.root = tree.getroot()
        return self.root