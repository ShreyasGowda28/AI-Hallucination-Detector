import re


def clean_text(text):
    """
    Remove Markdown formatting before sentence splitting.
    """

    # Remove bold markers (**text**)
    text = re.sub(r"\*\*", "", text)

    # Remove bullet points
    text = re.sub(r"^\s*[-*]\s*", "", text, flags=re.MULTILINE)

    # Remove numbered list markers like "1." or "2."
    text = re.sub(r"^\s*\d+\.\s*", "", text, flags=re.MULTILINE)

    # Replace multiple blank lines with a single newline
    text = re.sub(r"\n+", "\n", text)

    return text.strip()