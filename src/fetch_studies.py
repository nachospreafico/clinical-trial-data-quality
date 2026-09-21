import json
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "lung_cancer_studies.json"

URL = "https://clinicaltrials.gov/api/v2/studies"

params = {
    "query.cond": "lung cancer",
    "pageSize": 100,
    "format": "json",
}

# Request the first page of matching studies.
response = requests.get(URL, params=params, timeout=30)
response.raise_for_status()

# Convert the response into Python objects.
data = response.json()

# Save the full response before extracting any fields.
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("Studies downloaded:", len(data["studies"]))
print("Saved to:", OUTPUT_PATH)