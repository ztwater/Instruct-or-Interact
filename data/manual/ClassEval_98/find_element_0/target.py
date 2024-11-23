class XMLProcessor:
    def find_element(self, element_name):
        elements = self.root.findall(element_name)
        return elements