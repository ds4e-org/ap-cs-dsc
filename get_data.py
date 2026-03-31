# Download the data for the project
from pathlib import Path as P
import urllib.request as u

p = P.home()/'.local/share/datasets/hsclass1.txt'
p.parent.mkdir(parents=True, exist_ok=True)
p.exists() or u.urlretrieve('https://raw.githubusercontent.com/ds4e-org/ap-cs-dsc/refs/heads/main/data/hsclass1.txt')
print(f"Data now avaialbel at {p}")