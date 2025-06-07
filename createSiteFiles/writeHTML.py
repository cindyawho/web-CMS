def writeHTMLFile(name, hobbies):
    print("Writing HTML File...")
    print(f"Received: {name} and {hobbies}")
    hobbyList = hobbies.split(",")
    with open('createUserPage/userOutputFiles/index.html', 'w') as f:
        # write beginning and html head
        f.writelines(["<!DOCTYPE html>\n", "<head>\n", "\t<title>My Hobbies and Interests</title>\n", '\t<link rel="stylesheet" href="styles.css">\n', "</head>\n"])
        # write body
        f.writelines(["<body>\n", f"\t<h1>{name}</h1>\n", "\t<div class='hobbies'>\n", "\t\t<h2>My Hobbies</h2>\n"])
        f.write("\t\t<p>These are some of the things I like to do during my free time!</p>\n")
        f.write("\t\t<ul>\n")
        for i in range(len(hobbyList)):
            f.write(f"\t\t\t<li>{hobbyList[i]}</li>\n")
        f.write("\t\t</ul>\n")
        # write closing
        f.writelines(["</body>\n", "</html>"])