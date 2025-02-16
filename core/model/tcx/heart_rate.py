from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et
from core.model.tcx.tcx_constants import VALUE_TAG

class HeartRate:
    

    def __init__(self, element_tree: Element):
        self.__build_heart_rate(element_tree)


    def __build_heart_rate(self, element_tree: Element):
        if element_tree is not None:
            value_element = extract_tag_from_et(element_tree, VALUE_TAG)
            self.value = float(value_element.text)


    def __str__(self):
        return to_json(self)