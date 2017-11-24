import json
import sys

def load_data(filepath):
    with open(filepath) as opened_file:
        return json.load(opened_file)
        
def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4,                                      ensure_ascii=False)) 

if __name__ == '__main__':
    filepath = sys.argv[1]
    json_content = load_data(filepath)
    pretty_print_json(json_content)