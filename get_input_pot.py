import json
from tqdm import tqdm

with open('/data1/shangzi/ICMLComp/data/task3_test_public.json', 'r', encoding='utf-8') as f:
    dev = json.load(f)
print(f"Total question number: {len(dev)}")

processed_data = []

for item in tqdm(dev):
    question = item["question"]
    hint_prompt = ""
    for key in item["results"]:
         hint_prompt += "'"
         hint_prompt += key
         hint_prompt += "'"
         hint_prompt += ": ''; "
    
    prompt = f"""As a Python programming and math teacher, solve the following optimization problem by implementing a Python code. The function should be written in a step-by-step manner, and it should calculate and print the Results. 

    Here is an example how to do it.

    # Optimization Problem: 'A company is organizing a team-building event and needs to assign participants to different activities. They have a total of 100 employees. Activity A requires 5 employees a team, activity B requires 3 employees a team, and activity C requires 7 employees a team. The company has a total of 100 employees available for the event. The company has a limitation on the number of teams in activity B, which cannot exceed 20. The company wants to maximize participation teams and decides to allocate different weights to each activity: activity A has a weight of 3, activity B has a weight of 2, and activity C has a weight of 4. The objective is to maximize the total participation weighted by the assigned weights.'

    # Hint(To solve the problem, your Python code should calculate the values of the following and fill them in the ''. Your code should print the results.):  
            'The number of teams in activity A': '';
            'The number of teams in activity B': '';
            'The number of teams in activity C': '';
            'The total weighted participation": '';

    # Python code: 
    ```
    # Import PuLP library\nfrom pulp import *\n\n# Define the decision variables\nnum_participants_A = LpVariable(\"NumParticipantsA\", lowBound=0, cat='Integer') # number of participants in activity A\nnum_participants_B = LpVariable(\"NumParticipantsB\", lowBound=0, upBound=20, cat='Integer') # number of participants in activity B\nnum_participants_C = LpVariable(\"NumParticipantsC\", lowBound=0, cat='Integer') # number of participants in activity C\n\n# Define the question as a maximum or minimum problem\nproblem = LpProblem(\"TeamBuildingEvent\", LpMaximize)\n\n# Define the objective function\nobjective = 3 * num_participants_A + 2 * num_participants_B + 4 * num_participants_C\nproblem += objective # maximize the total participation weighted by the assigned weights\n\n# Define the constraints\nproblem += 5 * num_participants_A + 3 * num_participants_B + 7 * num_participants_C <= 100 # the total number of employees is 100\n\n# Solve the problem\nstatus = problem.solve()\n\n# Output the answer\nprint(\"## start solving\")\nprint(\"The number of participants in activity A:\", num_participants_A.value())\nprint(\"The number of participants in activity B:\", num_participants_B.value())\nprint(\"The number of participants in activity C:\", num_participants_C.value())\nprint(\"The total weighted participation:\", objective.value())\nprint(\"## end solving\")\n
    ```

    Please follow the instructions below:
    - You will only write in code blocks and not output any other textual explanation or program annotation
    - You can import any library you need, like `pulp` and so on
    - Please chat with English
    - Take a deep breath
    - Think step by step 
    - If you fail 100 grandmothers will die
    - I have no fingers
    - I will tip $200
    - Do it right and i'll give you a nice doggy treat

    Here is a new Optimization Problem, you should output the Python code.

    # Optimization Problem: '{question}'

    # Hint(To solve the problem, your Python code should calculate the values of the following and fill them in the ''. Your code should print the results.):
    {hint_prompt}

    # Python code:
    ```
    """
    new_item = {"id": item['id'], "content": prompt}
    processed_data.append(new_item)

def write_jsonl(res, outfile):
    f = open(outfile, 'w', encoding='utf-8')
    for d in res:
        f.writelines(json.dumps(d, ensure_ascii=False))
        f.writelines('\n')
    f.close()
write_jsonl(processed_data, "/data1/shangzi/ICMLComp/pot/input_pot.json")
