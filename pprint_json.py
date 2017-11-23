import json
import sys

def load_data(filepath):
    return json.load(open(filepath))

def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4))

if __name__ == '__main__':
    namespace = sys.argv[1]
    json_content = load_data(namespace)
    pretty_print_json(json_content)