from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_text_from_et_tag, extract_tag_from_et, extract_tags_from_et
from core.model.tcx.lap import Lap
from core.model.tcx.creator import Creator
from core.model.tcx.tcx_constants import ID_TAG, CREATOR_TAG, LAP_TAG

class Activity :
    

    def __init__(self, element_tree: Element):
        self.__build_activity(element_tree)
        self.__build_creator(element_tree)


    def __build_activity(self, element_tree: Element):
        if element_tree is not None:
            self.id = extract_text_from_et_tag(element_tree, ID_TAG)
            self.laps = [Lap(lap_element)
                         for lap_element
                         in extract_tags_from_et(element_tree, LAP_TAG)]


    def __build_creator(self, element_tree: Element):
        self.creator = Creator(extract_tag_from_et(element_tree, CREATOR_TAG))


    def __str__(self):
        return to_json(self)