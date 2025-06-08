import json
from pathlib import Path

def writeJSONfile(name, siteTitle, bookTitle, author, date, rating, desc, coverImg, spoilers, footer):
    jsonFilePath = Path('server/user.json')
    data = {}

    data["userName"] = name
    data["title"] = siteTitle
    data["journalTitle"] = "Latest Book I've Read"
    data["bookEntries"] = []
    data["bookEntries"].append({  
        "date": date,
        "title": bookTitle,
        "author": author,
        "coverURL": coverImg,
        "rating": rating,
        "description": desc,
        "spoilers": spoilers
    })
    data["footerDescription"]=footer

    with open(jsonFilePath, 'w') as outfile:  
        json.dump(data, outfile)