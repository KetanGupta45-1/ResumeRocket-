import re

def expand_compound_skill(skill):
    skill = skill.strip()
    if '&' in skill or ' and ' in skill:
        parts = re.split(r'&| and ', skill)
        return [p.strip() for p in parts if p.strip()]
    if '/' in skill:
        parts = skill.split('/')
        return [p.strip() for p in parts if p.strip()]
    return [skill]