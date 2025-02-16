from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et, extract_text_from_et_tag
from core.model.tcx.version import Version
from core.model.tcx.tcx_constants import NAME_TAG, PRODUCT_ID_TAG, VERSION_TAG

class Creator:
    

    def __init__(self, element_tree: Element):
        self.__build_creator(element_tree)


    def __build_creator(self, element_tree: Element):
        if element_tree is not None:
            self.name = extract_text_from_et_tag(element_tree, NAME_TAG)
            self.product_id = extract_text_from_et_tag(element_tree, PRODUCT_ID_TAG)
            self.build = Version(extract_tag_from_et(element_tree, VERSION_TAG))


    def __str__(self):
        return to_json(self)