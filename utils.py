from pathlib import Path
import urllib.request as u

def get_data(
    filename,
    base_url="https://raw.githubusercontent.com/ds4e-org/ap-cs-dsc/main/data/",
    folder="data"
):
    folder_path = Path(folder)
    path = folder_path / filename

    # Check if folder exists
    if not folder_path.exists():
        print(f"Creating folder: {folder_path}")
        folder_path.mkdir(parents=True)

    # Check if file exists
    if path.exists():
        print(f"File already exists: {path}")
    else:
        url = base_url + filename
        print(f"Downloading {filename}...")
        u.urlretrieve(url, path)
        print(f"Saved to {path}")

    return path