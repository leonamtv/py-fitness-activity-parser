from xml.etree.ElementTree import Element
from core.utils.serialization import to_json
from core.xml_utils.extractor import extract_text_from_et_tag, extract_tag_from_et
from core.model.tcx.track import Track
from core.model.tcx.heart_rate import HeartRate
from core.model.tcx.tcx_constants import TOTAL_TIME_SECONDS_TAG, START_TIME_ATTR, DISTANCE_METERS_TAG, \
                                         MAXIMUM_SPEED_TAG, CALORIES_TAG, INTENSITY_TAG, TRIGGER_METHOD_TAG, \
                                         TRACK_TAG, AVERAGE_HEART_RATE_BPM_TAG, MAXIMUM_HEART_RATE_BPM_TAG

class Lap:


    def __init__(self, element_tree: Element):
        self.__build_lap(element_tree)


    def __build_lap(self, element_tree: Element):
        if element_tree is not None:
            self.start_time = element_tree.get(START_TIME_ATTR)
            
            self.total_time_seconds = extract_text_from_et_tag(element_tree, TOTAL_TIME_SECONDS_TAG)
            self.distance_meters = extract_text_from_et_tag(element_tree, DISTANCE_METERS_TAG)
            self.maximum_speed = extract_text_from_et_tag(element_tree, MAXIMUM_SPEED_TAG)
            self.calories = extract_text_from_et_tag(element_tree, CALORIES_TAG)
            self.intensity = extract_text_from_et_tag(element_tree, INTENSITY_TAG)
            self.triggered_method = extract_text_from_et_tag(element_tree, TRIGGER_METHOD_TAG)

            self.track = Track(extract_tag_from_et(element_tree, TRACK_TAG))
            self.average_heart_rate = HeartRate(extract_tag_from_et(element_tree, AVERAGE_HEART_RATE_BPM_TAG))
            self.maximum_heart_rate = HeartRate(extract_tag_from_et(element_tree, MAXIMUM_HEART_RATE_BPM_TAG))

    
    def __str__(self):
        return to_json(self)