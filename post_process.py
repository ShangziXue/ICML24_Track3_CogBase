import json
import re

with open(f'/data1/shangzi/ICMLComp/results/results.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
with open(f'/data1/shangzi/ICMLComp/data/task3_test_public.json', 'r', encoding='utf-8') as f:
    test = json.load(f)

dict = {}
for item in test:
     k = 0
     for key in item["results"]:
          k += 1
     dict[item["id"]] = k
   

with open(f'/data1/shangzi/ICMLComp/results/result_var_count.json', 'w', encoding='utf-8') as f:
        json.dump(dict,f, ensure_ascii = False)          
        
def extract_and_format_numbers(text):
    numbers = re.findall(r":\s*(?:\$)?\s*'?[\d,]+\.?\d*'?|:\s*'?\$[\d,]+\.?\d*'?", text)
    # Convert extracted numbers to float, removing commas, dollar signs, and extra quotes
    converted_numbers = []
    for number in numbers:
        # Remove commas, dollar signs, quotes, and the leading colon with space
        cleaned_number = number.replace(',', '').replace('$', '').replace("'", "").replace(":", "").strip()
        # Determine how many decimal places the original number had
        decimal_places = cleaned_number[::-1].find('.')
        # Ensure conversion to float
        converted_number = float(cleaned_number)
        # Adjust decimal places: if there was no decimal point, set to 1; otherwise keep original
        if decimal_places == -1:
            converted_number = round(converted_number, 1)
        else:
            converted_number = round(converted_number, decimal_places)
        converted_numbers.append(converted_number)
    return converted_numbers

processed = []
for item in res:
      processed_dic = {}
      processed_dic["id"] = item["id"]
      processed_dic["question"] = item["question"]
      k = dict[item["id"]]
      text = item["print_results"]
      numbers = extract_and_format_numbers(text)
      last_k_numbers = numbers[-k:]
      results_dic = test[item["id"]]["results"]
      key_list = list(results_dic.keys())
      for i in range(len(last_k_numbers)):
            results_dic[key_list[i]] = str(last_k_numbers[i])
      processed_dic["results"] = results_dic 
      processed.append(processed_dic)
      

with open(f'/data1/shangzi/ICMLComp/results/prediction.json', 'w', encoding='utf-8') as f:
        json.dump(processed,f, indent=4, ensure_ascii = False)