import os
import json
from tqdm import tqdm
import openai
import time

openai.api_base = "https://api.openai-forward.com/v1"

dir_path = "/data1/shangzi/ICMLComp/pot/codes"

def ask_chatgpt(prompt_text):
    rsp = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ]
    )
    response_txt = rsp.choices[0].message.content.strip()
    return response_txt

def load_jsonl(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            data.append(d)
    return data
dev = load_jsonl("/data1/shangzi/ICMLComp/pot/input_pot.json")

res_list = []

openai.api_key = "your-api-key-here"
for item in tqdm(dev):
    time.sleep(20)
    dic = {}
    id = item["id"]
    dic["id"] = id
    prompt = item["content"]
    response = ask_chatgpt(prompt)
    print(response)
    dic['code'] = response
    res_list.append(dic)
    
with open(os.path.join(dir_path,"pot_codes.json"), 'w', encoding='utf-8') as f:
        json.dump(res_list,f, indent=4, ensure_ascii = False)


     
