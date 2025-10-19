import json

def extract_section(json_path, key=None):
    """
    Extract structured resume sections (Projects, Work Experience, Achievements)
    from a nested JSON file.

    Args:
        json_path (str): Path to the JSON resume file.
        key (str, optional): Specific section to extract 
            ("Projects", "Work Experience", "Achievements").

    Returns:
        dict: Structured dictionary with keys:
            - "projects"
            - "workExperience"
            - "achievements"
        Each contains a list of dicts with 'title'/'projectTitle' and 'description' list.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading JSON file '{json_path}': {e}")
        return {}

    key_map = {
        "Projects": "projects",
        "Work Experience": "workExperience",
        "Achievements": "achievements"
    }

    # Validate and decide keys to extract
    if key:
        if key not in key_map:
            print(f"⚠️ Invalid key '{key}'. Valid keys are: {list(key_map.keys())}")
            return {}
        json_keys_to_extract = [key]
    else:
        json_keys_to_extract = key_map.keys()

    output = {v: [] for v in key_map.values()}

    for json_key in json_keys_to_extract:
        struct_key = key_map[json_key]
        items = data.get(json_key, [])

        if not isinstance(items, list):
            print(f"⚠️ Expected list for '{json_key}', got {type(items).__name__}. Skipping.")
            continue

        for i, item in enumerate(items):
            if not isinstance(item, dict):
                print(f"⚠️ Skipping invalid entry {i} in '{json_key}' (not a dict).")
                continue

            # Select title key and title value
            title_key = "projectTitle" if struct_key == "projects" else "title"
            title = (
                item.get("project_name")
                or item.get("job_title")
                or item.get("achievement_title")
                or item.get("title")
                or ""
            )

            if not isinstance(title, str):
                print(f"⚠️ Invalid title type in '{json_key}'[{i}] — expected string.")
                title = ""

            title = title.strip()

            # Extract descriptions safely
            descriptions = []

            # Handle different possible field names
            possible_desc_keys = ["descriptions", "description", "points"]

            for desc_key in possible_desc_keys:
                desc_data = item.get(desc_key)
                if not desc_data:
                    continue

                if isinstance(desc_data, list):
                    descriptions.extend(
                        d.strip() for d in desc_data if isinstance(d, str) and d.strip()
                    )
                elif isinstance(desc_data, str) and desc_data.strip():
                    descriptions.append(desc_data.strip())

            if not descriptions:
                print(f"⚠️ No valid descriptions found in '{json_key}'[{i}].")

            output[struct_key].append({
                title_key: title,
                "description": descriptions
            })

    print(f"✅ Extracted sections summary: {{ {', '.join(f'{k}: {len(v)}' for k,v in output.items())} }}")
    return output
