import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilities import ChatTemplate

# Setup paths
current_dir = os.path.dirname(__file__)
folder_name = 'cinema'
cinema_path = os.path.join(current_dir, folder_name)
output_file = os.path.join(current_dir, 'cinema.jsonl')

template_path = os.path.join(current_dir, 'jsonl.json')
template = ChatTemplate.from_file(template_path)

jsonl = ''
for f in os.listdir(cinema_path):
    with open(os.path.join(cinema_path, f), 'r', encoding="utf-8", errors="ignore") as file:
        text = file.read()

    response = template.completion({'info': text, 'n': '20'})

    for line in response.choices[0].message.content.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            json.loads(line)  #test for valid JSON
            jsonl += line + '\n'
        except json.JSONDecodeError as e:
            print(f"Skipping line due to JSON error: {e}")
            continue

with open(output_file, 'w+', encoding="utf-8") as f:
    f.write(jsonl)

print(f"Done! Valid JSONL entries written to {output_file}")
