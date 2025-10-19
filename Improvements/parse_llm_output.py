def parse(raw_output):
    """
    Parse raw LLM output text into a clean list of improved bullet points.
    """

    improved = []
    for line in raw_output.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit() and (". " in line or ") " in line):
            line = line.split(". ", 1)[-1] if ". " in line else line.split(") ", 1)[-1]
        improved.append(line)
    return improved
