from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tags_from_et
from xml.etree.ElementTree import Element
from core.model.tcx.activity import Activity
from core.model.tcx.tcx_constants import ACTIVITY_TAG

class Activities:


    def __init__(self, element_tree: Element):
        self.activity_list = []
        self.creator = None
        self.__build_activity_list(element_tree)
        

    def __build_activity_list(self, element_tree: Element):
        self.activity_list = [Activity(activity_element) 
                              for activity_element 
                              in extract_tags_from_et(element_tree, ACTIVITY_TAG)]        


    def __str__(self):
        return to_json(self)