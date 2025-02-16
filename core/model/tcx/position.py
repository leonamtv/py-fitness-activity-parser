from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et
from core.model.tcx.tcx_constants import LATITUDE_TAG, LONGITUDE_TAG

class Position:
    

    def __init__(self, element_tree: Element):
        self.__build_position(element_tree)


    def __build_position(self, element_tree: Element):
        if element_tree is not None:
            latitude_element = extract_tag_from_et(element_tree, LATITUDE_TAG)
            longitude_element = extract_tag_from_et(element_tree, LONGITUDE_TAG)
            self.latitude_degrees = float(latitude_element.text)
            self.longitude_degrees = float(longitude_element.text)


    def __str__(self):
        return to_json(self)