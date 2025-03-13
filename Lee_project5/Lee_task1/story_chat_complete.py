import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))  # Add the project path to the system path

from utilities import ChatTemplate 


response1 = ChatTemplate.from_file('/Users/kodi.lee/ITS_595/Lee_project5/Lee_task1/story_chat.json').completion(
    {'characters': 'An Ant and a Human',
     'setting': 'Beautiful Brazilian Forest with a river',
     'conflict': 'The Ant is discovered by a Human and the Human wants to capture the Ant for scientific purposes.'})

print(response1.choices[0].message.content, "\n")

response2 = ChatTemplate.from_file('/Users/kodi.lee/ITS_595/Lee_project5/Lee_task1/story_chat.json').completion(
    {'characters': 'a feather pen and books',
     'setting': 'A vast library with the equivalence of alexandria.',
     'conflict': 'The books crave for ink like an addiction waiting to be satisfied, searching for the pen as he hides.'})

print(response2.choices[0].message.content, "\n")

response3 = ChatTemplate.from_file('/Users/kodi.lee/ITS_595/Lee_project5/Lee_task1/story_chat.json').completion(
    {'characters': 'An acorn and a white squirrel',
     'setting': 'Gallaudet University\'s old campus with large oak trees and a small pond',
     'conflict': 'The squirrel is preparing for winter until the acorns create a revolution: the acorns will not be silenced and their attempts to expose tyranny buried.'})

print(response3.choices[0].message.content, "\n")