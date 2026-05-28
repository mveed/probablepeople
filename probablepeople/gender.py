import json
import os

with open(os.path.join(os.path.dirname(__file__), "gender_names.json")) as f:
    gender_names = json.load(f)
