from pathlib import Path
from markdownify import markdownify as md


def html_to_markdown(html_file_path: Path) -> str:
    with open(html_file_path, "r") as file:
        return md(file.read())
