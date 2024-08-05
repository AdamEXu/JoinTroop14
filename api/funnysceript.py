import os
import json
# all images are stored under static/resources/photos folder
# they are then split into folders by category
# then print out the json output in format:
"""
[
  {
    "url": "/static/resources/photos/CATEGORY/FILENAME",
    "alt": "CATEGORY"
  },
  ...
]
"""

# get from photos.txt and output in json format
category = ""
photos = []
with open('photos.txt', 'r') as f:
  photos_list = f.readlines()

for line in photos_list:
  if line.strip().startswith("http"):
    photos.append({
      "url": line.strip(),
      "alt": category
    })
  elif line.strip() != "":
    category = line.strip()

print(json.dumps(photos))