# data_annotation_problem.py
import requests
from bs4 import BeautifulSoup


def decode_secret_message(doc_url: str) -> None:
    # 1) Get the published Google Doc page
    response = requests.get(doc_url, timeout=30)
    response.raise_for_status()

    # 2) Parse the HTML table rows
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")

    # Store characters by coordinate: (x, y) -> char
    points = {}

    for row in rows:
        cells = row.find_all(["td", "th"])
        if len(cells) != 3:
            continue

        col0 = cells[0].get_text(strip=True)
        col1 = cells[1].get_text(strip=True)
        col2 = cells[2].get_text(strip=True)

        # Skip header row like: x-coordinate | Character | y-coordinate
        try:
            x = int(col0)
            ch = col1
            y = int(col2)
        except ValueError:
            continue

        points[(x, y)] = ch

    if not points:
        print("No valid grid data found.")
        return

    # 3) Find grid size
    max_x = max(x for (x, _) in points.keys())
    max_y = max(y for (_, y) in points.keys())

    # 4) Print rows top -> bottom.
    #    Any missing coordinate is a space.
    for y in range(max_y, -1, -1):
        row_chars = []
        for x in range(max_x + 1):
            row_chars.append(points.get((x, y), " "))
        print("".join(row_chars))


if __name__ == "__main__":
    test_url = "https://docs.google.com/document/d/e/2PACX-1vSFTq6KR8ER5h9_bFVliDvYBntK6Wv8L7x6hLp2Sm58Zkhpo7Vsba9BmC82wcy8WoR3Q47J-brCiH3c/pub"
    decode_secret_message(test_url)
