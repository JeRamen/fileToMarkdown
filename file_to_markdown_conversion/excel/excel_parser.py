import pandas as pd
from pathlib import Path


def read_csv_file(csv_file_path: Path) -> ...:
    csvdf = pd.read_csv(csv_file_path)

    return csvdf.to_markdown()


def read_excel_file(excel_file_path: Path) -> ...:
    exdf = pd.read_excel(excel_file_path)

    return exdf.to_markdown()
