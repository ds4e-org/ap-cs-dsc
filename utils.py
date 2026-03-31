from pathlib import Path
import urllib.request as u

def get_data(url, filename, folder=".local/share/data"):
    path = Path.home() / folder / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        u.urlretrieve(url, path)

    return path