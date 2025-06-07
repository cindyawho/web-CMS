def writeHTMLFile(name, siteTitle="Personal Book Journal"):
    print("Writing HTML File...")
    print(f"Received: {name} and {siteTitle}")
    with open('createUserPage/userOutputFiles/index.html', 'w') as f:
        # write beginning and html head
        f.writelines(["<!DOCTYPE html>\n", "<html lang='en'>\n" "<head>\n", "\t<meta charset='UTF-8'>\n", '\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',f"\t<title>{siteTitle}</title>\n", '\t<link rel="stylesheet" href="styles.css">\n', "</head>\n"])

        # write body
        f.writelines(["<body>\n", "\t<div class='header'>\n",f"\t<h2>{name}</h2><div></div>\n", f"\t<div></div><h1>{siteTitle}</h1>\n"])
        f.write("\t\t<h2 class='latestHeading'>Latest Book I've Read</h2>\n")

        # write closing
        f.writelines(["</body>\n", "</html>"])