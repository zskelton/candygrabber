# IMPORTS
from urllib.request import urlopen
import json

# GLOBALS
url = "https://licorice.com/products/half-n-half"

# FUNCTIONS

# MAIN
def main():
  with urlopen(url) as f:
    resp = json.load(f)
  print(json.dumps(parsed, indent=2 ))

# RUN
if __name__ == '__main__':
    main()
