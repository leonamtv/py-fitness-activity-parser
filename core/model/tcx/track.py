from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tags_from_et
from core.model.tcx.track_point import TrackPoint
from core.model.tcx.tcx_constants import TRACK_POINT_TAG

class Track:


    def __init__(self, element_tree: Element):
        self.__build_track(element_tree)


    def __build_track(self, element_tree: Element):
        if element_tree is not None:
            self.track_points = [TrackPoint(track_point_element)
                                 for track_point_element
                                 in extract_tags_from_et(element_tree, TRACK_POINT_TAG)]

            
    def __str__(self):
        return to_json(self)