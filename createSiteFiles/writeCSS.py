def writeCSSFile(bgColor="#affde3", fontFamily="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;"):
    print("Writing CSS File...")
    print(f"Received: {bgColor} and {fontFamily}")
    with open('createUserPage/userOutputFiles/styles.css', 'w') as f:
        # * styles
        f.writelines(["* {\n", "\tbox-sizing: border-box;\n", "}\n\n"])
        # body styles
        f.writelines(["body {\n", f"\tbackground: {bgColor};\n", f"\tfont-family: {fontFamily};\n", "\tpadding: 20px;\n", "}\n\n"])
        # h1 styles
        f.writelines(["h1 {\n", 
                      "\tbackground-color: #002ba1;\n", 
                      f"\tcolor: {bgColor};\n", 
                      "\tmargin: 20px auto;\n", 
                      "\twidth: fit-content;\n", 
                      "\tpadding: 20px 70px;\n", 
                      "\tborder-radius: 20px;\n", 
                      "\tanimation-name: slideDown;\n", 
                      "\tanimation-duration: 5s;\n", 
                      "}\n\n"])
        # .hobbies styles
        f.writelines([".hobbies h2, .hobbies p, .hobbies ul {\n", 
                      "\tmargin: 20px auto;\n", 
                      "\twidth: fit-content;\n", 
                      "}\n\n"])
        # keyframes
        f.writelines(["@keyframes slideDown {\n", 
                      "\tfrom {\n", 
                      "\t\tmargin: -70px auto;\n",
                      "\t } \n"
                      "\to {\n", 
                      "\t\tmargin: 20px auto;\n",
                      "\t } \n"
                      "}\n\n"])