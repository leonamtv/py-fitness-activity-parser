import unittest
import xml.etree.ElementTree as ET

from xml.dom import minidom
from core.xml_utils.extractor import extract_tag_from_et, extract_tags_from_et, extract_text_from_et_tag

class ExtractorTest(unittest.TestCase):
    """
    Test cases for xml_utils.extractor
    """

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.payload = \
r"""<?xml version="1.0" encoding="UTF-8"?>
<BaseElement>
    <Activities>
        <Activity Sport="Other">
        <Id>2025-02-15T20:19:48.000Z</Id>
        <Lap StartTime="2025-02-15T20:19:48.000Z">
        </Lap>
        </Activity>
    </Activities>
    <Activities>
        <Activity Sport="Other">
        <Id>2025-02-15T20:19:48.000Z</Id>
        <Lap StartTime="2025-02-15T20:19:48.000Z">
        </Lap>
        </Activity>
    </Activities>
</BaseElement>"""

    def test_extract_tag_from_et_test_case_a(self):
        """
        Testing extract_tag_from_et -> successful scenario
        """
        expected_output = b'<?xml version="1.0" encoding="utf-8"?><Activities>\n        <Activity Sport="Other">\n        <Id>2025-02-15T20:19:48.000Z</Id>\n        <Lap StartTime="2025-02-15T20:19:48.000Z">\n        </Lap>\n        </Activity>\n    </Activities>'
        root = ET.ElementTree(ET.fromstring(self.payload))
        activities_element = extract_tag_from_et(root, './/Activities')
        activities_subtree = minidom.parseString(ET.tostring(activities_element)).toxml(encoding='utf-8')
        self.assertEqual(expected_output, activities_subtree)

    def test_extract_tag_from_et_test_case_b(self):
        """
        Testing extract_tag_from_et -> empty scenario
        """
        expected_output = None
        root = ET.ElementTree(ET.fromstring(self.payload))
        activities_element = extract_tag_from_et(root, './/Activitie')
        self.assertEqual(expected_output, activities_element)

    def test_extract_tags_from_et_test_case_a(self):
        """
        Testing extract_tags_from_et -> successful scenario
        """
        root = ET.ElementTree(ET.fromstring(self.payload))
        activities_elements = extract_tags_from_et(root, './/Activity')
        
        self.assertEqual(len(activities_elements), 2)

    def test_extract_tags_from_et_test_case_b(self):
        """
        Testing extract_tags_from_et -> empty scenario
        """
        root = ET.ElementTree(ET.fromstring(self.payload))
        activities_elements = extract_tags_from_et(root, './/Activit')
        
        self.assertEqual(len(activities_elements), 0)

    def test_extract_text_from_et_tag_test_case(self):
        """
        Testing extract_text_from_et_tag -> empty scenario
        """
        root = ET.ElementTree(ET.fromstring(self.payload))
        activities_elements = extract_tags_from_et(root, './/Activity')[0]
        id = extract_text_from_et_tag(activities_elements, './/Id')
        self.assertEqual(id, '2025-02-15T20:19:48.000Z')


if __name__ == '__main__':
    unittest.main()