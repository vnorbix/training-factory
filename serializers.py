
import json
import xml.etree.ElementTree as et

class JsonSerializer:
    def __init__(self) -> None:
        self._current_object = None

    def start_object(self, name, id):
        self._current_object = {
            'id': id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)

class XmlSerializer:
    def __init__(self) -> None:
        self._element = None

    def start_object(self, name, id):
        self._element = et.Element(name, attrib={'id': id})

    def add_property(self, name, value):
        if self._element is not None:
            prop = et.SubElement(self._element, name) 
            prop.text = value

    def to_str(self):
        if self._element is None:
            return ""
        return et.tostring(self._element, encoding='unicode')

class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

class SerializerFactory:

    def __init__(self) -> None:
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError()
        return creator()


factory = SerializerFactory()
factory.register_format("JSON", JsonSerializer)
factory.register_format("XML", XmlSerializer)