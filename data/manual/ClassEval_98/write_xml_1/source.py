class XMLProcessor:
    def write_xml(data, file_path):
        root = ET.Element("root")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(file_path)