#!/usr/bin/env python3

import json
import sys
from typing import Dict, List

def read_json_from_stdin() -> Dict:
    """Read and return the JSON data from standard input."""
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError:
        print("Error: Invalid JSON input.")
        raise
def json_to_file(json_data: Dict) -> List:
    # Writing the 'program' data to a file
    with open('program_compiled.json', 'w') as file:
        json.dump(json_data["program"], file, indent=2)

    # Writing the 'program_input' data to a file
    with open('program_input.json', 'w') as file:
        json.dump(json_data["program_input"], file, indent=2)

def main():
    program_public_input = read_json_from_stdin()
    json_to_file(program_public_input)

if __name__ == "__main__":
    main()
