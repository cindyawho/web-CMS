import json

def writeJSONfile(name, siteTitle, bookTitle, author, date, rating, desc, coverImg, spoilers, footer):
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

    with open('..\\server\\user.json', 'w') as outfile:  
        json.dump(data, outfile)