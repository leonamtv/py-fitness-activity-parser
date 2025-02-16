from datetime import datetime
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_tag_from_et, extract_text_from_et_tag
from xml.etree.ElementTree import Element
from core.model.tcx.position import Position
from core.model.tcx.heart_rate import HeartRate
from core.model.tcx.tcx_constants import TIME_TAG, POSITION_TAG, ALTITUDE_METERS_TAG, DISTANCE_METERS_TAG, \
                                         HEART_RATE_BPM_TAG

class TrackPoint:
    

    def __init__(self, element_tree: Element):
        self.__build_track(element_tree)


    def __build_track(self, element_tree: Element):
        if element_tree is not None:
            self.time = datetime.fromisoformat(extract_text_from_et_tag(element_tree, TIME_TAG))
            self.altitude_meters = float(extract_text_from_et_tag(element_tree, ALTITUDE_METERS_TAG))
            self.distance_meters = float(extract_text_from_et_tag(element_tree, DISTANCE_METERS_TAG))
            self.heart_rate = HeartRate(extract_tag_from_et(element_tree, HEART_RATE_BPM_TAG))
            self.position = Position(extract_tag_from_et(element_tree, POSITION_TAG))
            # TODO Extensions


    def __str__(self):
        return to_json(self)