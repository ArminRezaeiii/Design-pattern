import xml.etree.ElementTree as ET
import json


class XMLToJSONConverter:
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path
        self.json_data = None

    def parse_xml(self):

        try:
            tree = ET.parse(self.xml_file_path)
            root = tree.getroot()
            self.json_data = self._element_to_dict(root)
        except ET.ParseError as e:
            print(f"خطا در تجزیه XML: {e}")
        except FileNotFoundError:
            print("فایل XML پیدا نشد.")

    def _element_to_dict(self, element):

        data = {}


        if list(element):
            children = {}
            for child in element:
                child_data = self._element_to_dict(child)
                if child.tag not in children:
                    children[child.tag] = []
                children[child.tag].append(child_data)
            data[element.tag] = children
        else:

            data[element.tag] = element.text

        return data

    def get_json(self):

        if self.json_data is None:
            self.parse_xml()
        return json.dumps(self.json_data, ensure_ascii=False, indent=4)

    def save_json(self, output_file_path):
       
        if self.json_data is None:
            self.parse_xml()
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f, ensure_ascii=False, indent=4)
        print(f"فایل JSON با موفقیت ذخیره شد در: {output_file_path}")

if __name__ == "__main__":
    converter = XMLToJSONConverter("data.xml")
    converter.parse_xml()
    json_output = converter.get_json()
    print(json_output)
    converter.save_json("output.json")
