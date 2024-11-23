class XMLProcessor:
    def process_xml_data(input_file, output_file):
        # Parse the input XML file
        tree = ET.parse(input_file)
        root = tree.getroot()
    
        # Modify the data in XML elements
        for element in root.iter('element_to_modify'):
            # Modify the data as needed
            element.text = 'new_value'
    
        # Write the updated XML data to a new file
        tree.write(output_file)