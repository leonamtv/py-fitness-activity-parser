from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_text_from_et_tag
from core.model.tcx.tcx_constants import BUILD_MINOR_TAG, BUILD_MAJOR_TAG, VERSION_MINOR_TAG, VERSION_MAJOR_TAG

class Version:


    def __init__(self, element_tree: Element):
        self.build_major = extract_text_from_et_tag(element_tree, BUILD_MAJOR_TAG)
        self.build_minor = extract_text_from_et_tag(element_tree, BUILD_MINOR_TAG)
        self.version_major = extract_text_from_et_tag(element_tree, VERSION_MAJOR_TAG)
        self.version_minor = extract_text_from_et_tag(element_tree, VERSION_MINOR_TAG)

    
    def __str__(self):
        return to_json(self)