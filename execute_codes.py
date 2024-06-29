import io
import os
import sys
import json
from pulp import *
from tqdm import tqdm

in_path = "/data1/shangzi/ICMLComp/pot/codes/pot_codes.json"
out_path = "/data1/shangzi/ICMLComp/pot/results"

def execute_and_capture_output(code_text):
    # Create a string buffer to capture output
    captured_output = io.StringIO()
    # Backup the current standard output
    current_stdout = sys.stdout
    # Redirect standard output to the string buffer
    sys.stdout = captured_output
    
    try:
        # Execute the provided code text
        exec(code_text)
    except Exception as e:
        # If there is an error during execution, print it to the captured output
        print(f"An error occurred: {e}")
    finally:
        # Restore standard output to its original state
        sys.stdout = current_stdout
    
    # Get the content of captured output
    output = captured_output.getvalue()
    # Close the StringIO object
    captured_output.close()
    
    return output

with open(os.path.join(in_path,"gpt4turbo_pot_codes.json"), 'r', encoding='utf-8') as f:
    codes = json.load(f)

res_list = []

for key in codes:
    dic = {}
    dic["id"] = int(key)
    code = codes[key][0]
    output = execute_and_capture_output(code)
    dic["print_results"] = output
    res_list.append(dic)

with open(os.path.join(out_path,"results.json"), 'w', encoding='utf-8') as f:
        json.dump(res_list,f, indent=4, ensure_ascii = False)