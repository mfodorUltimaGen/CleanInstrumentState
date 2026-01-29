import xml.etree.ElementTree as ET
import sys

instrument_state_file = sys.argv[1] + '\\InstrumentState.xml'
# instrument_state_file = 'C:\\Projects\\Pegasus_3.0_QA\\State\\InstrumentState.xml'


field_dict = {
    "ChuckCfg": {
        "HasWafer": "true",
        "HasVacuum": "true",
        "WaferUsed": "true",
        "CeilingClean": "true"
    },
    "Needle": {
        "InUse": "false",
    },
    "BLS": {
        "HasWafer": "false",
        "HasVacuum": "false",
        "WaferUsed": "false",
    }
}


def update_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Update the fields from the dict
        for field_name, field_data in field_dict.items():
            update_fields(root, field_name, field_data)

        # Save the updated XML to a new file or overwrite the existing one
        updated_xml_file = xml_file.replace('.xml', '.xml')
        tree.write(updated_xml_file, encoding='utf-8', xml_declaration=True)

        print(f'Updates saved to {updated_xml_file}')
    except ET.ParseError:
        print("Error parsing the XML file. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_fields(root, field_name: str, field_data: dict) -> None:
    # Look for the provided field name
    for field_elem in root.iter(field_name):

        # Special case if a Chuck has a SampleID-- should be removed
        if field_name == 'ChuckCfg':
            if 'SampleId' in field_elem.attrib:
                del field_elem.attrib['SampleId']

        # Set the attribute to the proper state
        for field_attribute, field_state in field_data.items():
            field_elem.set(field_attribute, field_state)


update_xml(instrument_state_file)
