import json

def extract_skills(json_path):
    '''
    Extract Skills from the json.
    return skills in list form.
    '''


    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error while reading JSON file '{json_path}' -> {e}")
        return []

    skills = []

    if not isinstance(data, dict):
        print(f"Error: Expected JSON object (dict), but got {type(data).__name__}")
        return []

    if 'Skills' not in data:
        print(f"Error: Key 'Skills' not found in JSON data from '{json_path}'")
        return []

    raw_categories = data.get('Skills', [])
    if not isinstance(raw_categories, list):
        print(f"Error: 'Skills' should be a list, but got {type(raw_categories).__name__}")
        return []

    for i, category in enumerate(raw_categories):
        if not isinstance(category, dict):
            print(f"Warning: Skill category at index {i} is not a dict, skipping...")
            continue
        if 'skills' not in category:
            print(f"Warning: Missing 'skills' key in category at index {i}, skipping...")
            continue

        for skill in category['skills']:
            if isinstance(skill, str) and skill.strip():
                skills.append(skill.strip())
            else:
                print(f"Warning: Invalid skill format in category {i}: {skill}")

    if not skills:
        print(f"Warning: No valid skills found in '{json_path}'")

    print(f"Skills in resume '{json_path}': {skills}")
    return skills
