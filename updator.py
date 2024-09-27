import xml.etree.ElementTree as ET
import sys

instrumentStateFile = sys.argv[1] + '\\InstrumentState.xml'


def update_xml(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Example: Find elements by tag and attribute, and update their values
    for wafer_elem in root.iter('ChuckCfg'):
        if 'SampleId' in wafer_elem.attrib:
            del wafer_elem.attrib['SampleId']

        wafer_attributes = ['HasWafer', 'HasVacuum', 'WaferUsed', 'CeilingClean']
        for wafer_attribute in wafer_attributes:
            value = wafer_elem.attrib.get(wafer_attribute, '').lower()
            if value == 'false':
                wafer_elem.set(wafer_attribute, 'true')
    for bls_elem in root.iter('BLS'):
        bls_attributes = ['HasWafer', 'HasVacuum', 'WaferUsed']
        for bls_attribute in bls_attributes:
            value = bls_elem.attrib.get(bls_attribute, '').lower()
            if value == 'true':
                bls_elem.set(bls_attribute, 'false')

    for needle_elem in root.iter('Needle'):
        needle_in_use = needle_elem.attrib.get('InUse', '').lower()

        if needle_in_use == 'true':
            needle_elem.set('InUse', 'false')

    # Save the updated XML to a new file or overwrite the existing one
    updated_xml_file = xml_file.replace('.xml', '.xml')
    tree.write(updated_xml_file, encoding='utf-8', xml_declaration=True)

    print(f'Updated XML saved to {updated_xml_file}')



update_xml(instrumentStateFile)