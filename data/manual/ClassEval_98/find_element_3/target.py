class XMLProcessor:
    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        """
        root = self.read_xml()  # Call the read_xml method to get the root element
        elements = root.findall(element_name)  # Use the root element to find elements with the specified name
        return elements