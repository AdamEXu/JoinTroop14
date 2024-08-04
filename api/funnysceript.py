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

# first, convert them all to jpg
for category in os.listdir('static/resources/photos'):
  if category.endswith('.DS_Store'):
    continue
  else:
    for photo in os.listdir(f'static/resources/photos/{category}'):
      if photo.endswith('.jpg'):
        continue
      elif photo.endswith('.DS_Store'):
        continue
      else:
        print(photo)
        os.system(f"convert static/resources/photos/{category}/{photo} static/resources/photos/{category}/{photo.split('.')[0]}.jpg")
        rm = f"rm static/resources/photos/{category}/{photo}"

photos = []
for category in os.listdir('static/resources/photos'):
  if category.endswith('.DS_Store'):
    continue
  for photo in os.listdir(f'static/resources/photos/{category}'):
    if photo.endswith('.DS_Store'):
      continue
    if photo.endswith('.jpg'):
      photos.append({
          "url": f"/static/resources/photos/{category}/{photo}",
          "alt": category
      })
print(json.dumps(photos))