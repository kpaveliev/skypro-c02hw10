import json
import class_

# Importing candiates dictionary and assigning to class
def assign_class(filename):
    """Load file and assign class to all elements"""

    with open(filename, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)

    candidates = []

    for i in range(len(candidates_list)):
        candidates.append(class_.Candidate(candidates_list[i]['id'],
                                    candidates_list[i]['name'],
                                    candidates_list[i]['picture'],
                                    candidates_list[i]['position'],
                                    candidates_list[i]['gender'],
                                    candidates_list[i]['age'],
                                    candidates_list[i]['skills']
                                    ))

    return candidates

if __name__ == '__main__':
    candidates = assign_class('candidates.json')
    print(candidates[2].print_candidate())