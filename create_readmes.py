
"""
GOAL: Automatically create a README.md file for each of the many subfolders in this directory. Within each README.md, add a table (with 5 columns) to display all the wallpapers within that subfolder.

NOTE: I used ChatGPT to help make this
"""


from pathlib import Path
from urllib.parse import quote
import math

# Constants / Magic
ROOT = Path("./")
COLUMNS = 5
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def make_readme(subfolder: Path) -> None:
    # Create a subfolder's README.md and table

    images = sorted((
        file for file in subfolder.iterdir() 
        if file.is_file() and 
        file.suffix.lower() in IMAGE_EXTENSIONS), key=lambda path: path.name.lower()
    )

    lines = [
        f"# {subfolder.name}",
        "",
        f"{len(images)} pictures",
        "",
        "<table>",
    ]

    rows = math.ceil(len(images) / COLUMNS)
    for row in range(rows):
        lines.append("  <tr>")

        start = row * COLUMNS
        row_images = images[start: start + COLUMNS]

        for image in row_images:
            src = quote(image.name)

            lines.extend(
                [
                    "    <td align=\"center\">",
                    f'      <a href="src">',
                    f'        <img src="{src}" width="200"',
                    "      </a>",
                    "    </td>",
                ]
            )

        # If this is the last row, we add a few empty table entries
        for _ in range(COLUMNS - len(row_images)):
            lines.append("    <td></td>")

        lines.append("  </tr>")

    # End of README
    lines.extend(
        [
            "</table>"
            "",
            "<!-- This README was automatically generated with Python. -->",
            "",
        ]
    )

    readme = subfolder / "README.md"
    readme.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated {readme} ({len(images)} images)")


def delete_readme(subfolder):
    for readme in subfolder.rglob("README"):
        readme.unlink()
        print(f"Deleted: {readme}")


def main() -> None:
    folders = [ROOT]
    folders.extend(path for path in ROOT.rglob("*") if path.is_dir())

    for subfolder in folders:
        delete_readme(subfolder)
        make_readme(subfolder)


if __name__ == "__main__":
    main()