import json

def writeJSONfile(name, siteTitle="Personal Book Journal"):
    data = {}

    data["userName"] = name
    data["title"] = siteTitle
    data["journalTitle"] = "Latest Book I've Read"
    data["bookEntries"] = []
    data["bookEntries"].append({  
        "date":"2025-06-08",
        "title":"Foxglove",
        "author":"Adalyn Grace",
        "coverURL":"https://images.booksense.com/images/500/162/9780316162500.jpg",
        "rating":3.5,
        "description":"While the book moved a bit slow, the challenges that Signa face involve an interesting dynamic. If you're into slow-paced gothic books, try it out!",
        "spoilers":"I wanted to see more scenes with her powers of Life and Death. While Blythe is a spunky character, I felt like the story moved much slower with her perspective and would have preferred if it was just Signa and her exploring her powers. Aris, or Fate, is annoying and I don't prefer him at all, but every story needs a bad guy I guess."
    })
    data["footerDescription"]="Want to talk books? Send me an email at example@pcc.edu!"

    with open('data.json', 'w') as outfile:  
        json.dump(data, outfile)