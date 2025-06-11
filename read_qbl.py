import yaml
import json
from datetime import datetime

class QuickBaseLoader(yaml.FullLoader):
    """ Custom YAML Loader to handle QuickBase-specific structures. """

    def construct_qb_ref(self, node):
        """ Handles known `!Ref` tags by converting them into structured references. """
        if isinstance(node, yaml.ScalarNode):
            return {"Ref": self.construct_scalar(node)}
        elif isinstance(node, yaml.MappingNode):
            return self.construct_mapping(node)
        return None  # Fallback for unsupported cases

    def construct_unknown(self, tag, node):
        """ Fallback for unrecognized YAML tags—stores them as a dictionary instead of failing. """
        if isinstance(node, yaml.ScalarNode):
            return {tag: self.construct_scalar(node)}
        elif isinstance(node, yaml.MappingNode):
            return {tag: self.construct_mapping(node)}
        return {tag: None}  # Safely handle unexpected cases

# Register constructors
QuickBaseLoader.add_constructor('!Ref', QuickBaseLoader.construct_qb_ref)
QuickBaseLoader.add_multi_constructor('!', QuickBaseLoader.construct_unknown)  # Handles unknown tags properly

def json_serializable(obj):
    """ Converts datetime objects to JSON-compatible strings. """
    if isinstance(obj, datetime):
        return obj.isoformat()  # Converts to 'YYYY-MM-DDTHH:MM:SS'
    raise TypeError(f"Type {type(obj)} not serializable")

def load_yaml_to_json(file_path):
    """ Loads the YAML-like QuickBase file and converts it to JSON. """
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=QuickBaseLoader)

    json_output = json.dumps(data, indent=4, default=json_serializable)  # Convert datetime properly
    return json_output

# Example usage:
yaml_file = "simple_app_qbl.yaml"
json_data = load_yaml_to_json(yaml_file)
# print(json_data)
with open("simple_app_qbl.json", "w") as outfile:
    outfile.write(json_data)