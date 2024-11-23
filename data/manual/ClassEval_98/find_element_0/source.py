class XMLProcessor:
    def find_element(xml_string, element_name):
        root = ET.fromstring(xml_string)
        elements = root.findall(element_name)
        return elements