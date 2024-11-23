class XMLProcessor:
    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        root = ET.Element("root")
        for key, value in self.data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(file_name)
        return True