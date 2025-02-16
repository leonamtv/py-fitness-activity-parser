from xml.etree.ElementTree import Element

def extract_text_from_et_tag(element_tree: Element, tag: str) -> str:
    element = extract_tag_from_et(element_tree, tag)
    if element is None :
        return None
    return element.text

def extract_tag_from_et(element_tree: Element, tag: str) -> Element:
    elements = extract_tags_from_et(element_tree, tag)
    return None if len(elements) == 0 else elements[0]

def extract_tags_from_et(element_tree: Element, tag: str) -> list[Element]:
    return element_tree.findall(tag)