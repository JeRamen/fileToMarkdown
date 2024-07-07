from file_to_markdown_conversion.excel.excel_parser import (
    read_excel_file,
    read_csv_file,
)
from file_to_markdown_conversion.html_parser.html_parser import html_to_markdown
from file_to_markdown_conversion.image.text_from_image import get_text_from_image
from pathlib import Path

if __name__ == "__main__":
    excel_file_path = Path(__file__).parent.resolve() / "test_excel.xlsx"
    csv_file_path = Path(__file__).parent.resolve() / "test_csv.csv"
    html_file_path = Path(__file__).parent.resolve() / "test_html.html"
    image_file_path = Path(__file__).parent.resolve() / "test_image_png.png"

    print(f"Excel file to markdown output: \n {read_excel_file(excel_file_path)}")
    print(f"Csv file to markdown output: \n {read_csv_file(csv_file_path)}")
    print(f"Html file to markdown output: \n {html_to_markdown(html_file_path)}")
    print(f"Png file to markdown output: \n {get_text_from_image(image_file_path)}")
