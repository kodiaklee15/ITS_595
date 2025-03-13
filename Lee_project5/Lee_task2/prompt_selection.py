import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))  # Add the project path to the system path

from utilities import ChatTemplate 
import json

base_dir = os.path.dirname(__file__)  # Lee_task2 directory

selection_template_path = os.path.join(base_dir, 'selection_chat.json')
selectionTemplate = ChatTemplate.from_file(selection_template_path)

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break

    selection_response = selectionTemplate.completion({'ask': ask})
    selection = json.loads(selection_response.choices[0].message.content)

    # Dynamically choose the right JSON file (doctor_chat.json or engineer_chat.json)
    template_file_path = os.path.join(base_dir, f"{selection['as']}_chat.json")

    # Load the selected chat template
    chat_template = ChatTemplate.from_file(template_file_path)

    # Generate final completion using action and document
    response = chat_template.completion({
        'action': selection['action'],
        'document': selection['document']
    })
    
    print(response.choices[0].message.content)