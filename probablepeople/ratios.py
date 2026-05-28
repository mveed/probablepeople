import json
import os

with open(os.path.join(os.path.dirname(__file__), "ratios.json")) as f:
    ratios = json.load(f)