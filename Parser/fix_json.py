import re
import json
import ast

def fix_json(raw_text):
    """
    Cleans and fixes broken JSON-like text from resumes or exports.
    Returns a valid Python dict or None if recovery fails.
    """

    if not isinstance(raw_text, str) or not raw_text.strip():
        print("⚠️ Empty or invalid input text.")
        return None

    original = raw_text

    # 1️⃣ Normalize quotes and escape issues
    raw_text = raw_text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    raw_text = re.sub(r"\\'", "'", raw_text)  # fix escaped single quotes
    raw_text = re.sub(r'\\"{2,}', '"', raw_text)  # fix double-escaped quotes

    # 2️⃣ Fix GitHub/LinkedIn malformed links
    raw_text = re.sub(r'"github"\s*:\s*""https', r'"github": "https', raw_text)
    raw_text = re.sub(r'"linkedin"\s*:\s*""https', r'"linkedin": "https', raw_text)

    # 3️⃣ Remove trailing commas before } or ]
    raw_text = re.sub(r',\s*([}\]])', r'\1', raw_text)

    # 4️⃣ Ensure balanced brackets/braces
    diff_braces = raw_text.count('{') - raw_text.count('}')
    diff_brackets = raw_text.count('[') - raw_text.count(']')
    if diff_braces > 0:
        raw_text += '}' * diff_braces
    if diff_brackets > 0:
        raw_text += ']' * diff_brackets

    # 5️⃣ Try direct JSON parsing
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        pass

    # 6️⃣ Fallback: try repairing common patterns
    raw_text = re.sub(r'([{,]\s*)([A-Za-z0-9_]+)(\s*:)', r'\1"\2"\3', raw_text)  # unquoted keys
    raw_text = re.sub(r':\s*None\b', ': null', raw_text)
    raw_text = re.sub(r':\s*True\b', ': true', raw_text)
    raw_text = re.sub(r':\s*False\b', ': false', raw_text)

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON parsing still failed after fixes: {e}")

    # 7️⃣ Final fallback: literal_eval (handles pseudo-JSON)
    try:
        return ast.literal_eval(original)
    except Exception:
        print("❌ Could not recover valid JSON structure.")
        return None
