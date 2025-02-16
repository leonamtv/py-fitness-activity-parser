from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et
from core.model.tcx.tcx_constants import VERSION_TAG
from core.model.tcx.version import Version

class Build:


    def __init__(self, element_tree: Element):
        self.version = Version(extract_tag_from_et(element_tree, VERSION_TAG))


    def __str__(self):
        return to_json(self)
        