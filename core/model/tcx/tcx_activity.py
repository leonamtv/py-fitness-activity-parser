import xml.etree.ElementTree as et

from os import path
from core.model.basic_activity import BasicActivity
from core.xml_utils.extractor import extract_tags_from_et, extract_tag_from_et
from core.model.tcx.author import Author
from xml.etree.ElementTree import Element
from core.model.tcx.activities import Activities
from core.model.tcx.tcx_constants import ACTIVITIES_TAG, AUTHOR_TAG

class TCXActivity(BasicActivity):

    def __init__(self, file_path):
        if not path.exists(file_path) :
            raise FileNotFoundError
        self.file_path = file_path
        self.__build_tree(et.parse(self.file_path))


    def __build_tree(self, element_tree: Element):
        self.__build_activities(element_tree)
        self.__build_author(element_tree)


    def __build_activities(self, element_tree: Element):
        self.activities = [Activities(activities_element) 
                           for activities_element 
                           in extract_tags_from_et(element_tree, ACTIVITIES_TAG)]


    def __build_author(self, element_tree: Element):
        self.author = Author(extract_tag_from_et(element_tree, AUTHOR_TAG))

    def to_json(self):
        return super().to_json()

