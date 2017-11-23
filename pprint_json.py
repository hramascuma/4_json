import json
import sys

def load_data(filepath):
    return json.load(open(filepath))

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))

if __name__ == '__main__':
    namespace = sys.argv[1]
    data = load_data(namespace)
    pretty_print_json(data)