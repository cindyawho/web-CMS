def writeHTMLFile(name, siteTitle, bookTitle, author, date, rating, desc, coverImg):
    print("Writing HTML File...")
    print(f"Received: {name}, {siteTitle}, {bookTitle}, {author}, {date}, {rating}, {desc}, {coverImg}")
    with open('server\\userFiles\\index.html', 'w') as f:
        # write beginning and html head
        f.writelines(["<!DOCTYPE html>\n", "<html lang='en'>\n" "<head>\n", "\t<meta charset='UTF-8'>\n", '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',f"\t<title>{siteTitle}</title>\n", '\t<link rel="stylesheet" href="styles.css">\n', "</head>\n"])

        # write body
        f.writelines(["<body>\n", "\t<div class='header'>\n",f"\t\t<h2>{name}'s</h2><div></div>\n", f"\t\t<div></div><h1>{siteTitle}</h1>\n", "\t</div>"])
        f.write("\t<h2 class='latestHeading'>Latest Book I've Read</h2>\n")
        f.write("\t<div class='latestJournal'>\n")
        f.write("\t\t<div class='latestText'>\n")
        f.writelines(["\t\t\t<h3>Book Title</h3><div></div>\n", f"\t\t\t<div></div><p>By: {author}</p>\n", f"\t\t\t<p class='latestDate'>Finished Reading: {date}</p><div></div>\n", f"\t\t\t<div></div><p>Rating: {rating} stars</p>\n", f"\t\t\t<p class='latestDescription'>My Thoughts on the Book: {desc}</p>\n"])
        f.write("\t\t</div>\n")
        f.write("\t\t<div class='latestImage'>\n")
        f.write(f"\t\t\t<img src='{coverImg}' alt='Cover art of book'>\n")
        f.write("\t\t</div>\n")
        f.write("\t</div>\n")

        # write Footer
        f.write("\t<footer>\n")
        f.write(f"\t\t<p>{name}, 2025</p>\n")
        f.write("\t</footer>\n")
        # write closing
        f.writelines(["</body>\n", "</html>"])