from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et, extract_text_from_et_tag
from core.model.tcx.build import Build
from core.model.tcx.tcx_constants import NAME_TAG, LANG_ID_TAG, PART_NUMBER_TAG, BUILD_TAG

class Author:


    def __init__(self, element_tree: Element):
        self.__build_author(element_tree)


    def __build_author(self, element_tree: Element):
        if element_tree is not None:
            self.name = extract_text_from_et_tag(element_tree, NAME_TAG)
            self.lang_id = extract_text_from_et_tag(element_tree, LANG_ID_TAG)
            self.part_number = extract_text_from_et_tag(element_tree, PART_NUMBER_TAG)
            self.build = Build(extract_tag_from_et(element_tree, BUILD_TAG))
         
            
    def __str__(self):
        return to_json(self)
