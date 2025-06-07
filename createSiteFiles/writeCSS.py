def writeCSSFile(bgColor="#FFECD5", fontColor="black", fontFamily="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;"):
    print("Writing CSS File...")
    print(f"Received: {bgColor} and {fontFamily}")
    with open('createUserPage/userOutputFiles/styles.css', 'w') as f:
        # * styles
        f.writelines(["* {\n", "\tbox-sizing: border-box;\n", "}\n\n"])
        # body styles
        f.writelines(["body {\n", f"\tbackground: {bgColor};\n", f"\tfont-family: {fontFamily};\n", f"\tcolor: {fontColor};\n", "\tpadding: 20px;\n", "}\n\n"])
        
        # HEADER styles
        f.writelines(["\n/* ********************************************************** */\n/* ****************        HEADER       ********************* */\n/* ********************************************************** */\n\n"])
        f.writelines([".header{\n",
                      "\tdisplay: grid; grid-template-columns: auto auto; grid-template-rows: auto auto; margin: 100px 0 150px 0;",
                      "}\n\n"])
        f.writelines([".header h2{\n",
                      "\tborder-top: 4px solid black; text-align: right; padding-top: 20px;",
                      "}\n\n"])
        f.writelines([".header h1{\n",
                      "\tborder-bottom: 4px solid black; margin-top: 0; padding-bottom: 20px;",
                      "}\n\n"])
        
        # MAIN Styles
        f.writelines(["\n/* ********************************************************** */\n/* ****************        MAIN         ********************* */\n/* ********************************************************** */\n\n"])

        f.writelines([".latestHeading {\n",
                      "\tborder-bottom: 3px solid black; text-align: center;",
                      "}\n",
                      ".latestJournal {\n",
                      "\tdisplay: flex; flex-direction: row;padding: 0 20px;",
                      "}\n",
                      ".latestText {\n",
                      "\tdisplay: grid; grid-template-columns: auto auto; grid-template-rows: auto auto auto auto auto;",
                      "}\n"
                      ".latestText h3, .latestDate {\n",
                      "\ttext-align: right;",
                      "}\n",
                      ".latestDescription {\n",
                      "\tgrid-column: 1 / span 2;",
                      "}\n\n",
                      ])
        
        # FOOTER Styles
        f.writelines(["\n/* ********************************************************** */\n/* ****************        FOOTER         ********************* */\n/* ********************************************************** */\n\n"])
        f.writelines(["footer {\n",
                      "\tbackground-color: #7B6041; color: whitesmoke; width: 110%; height: 100px; margin: 50px 0 -15px -15px; display: flex; align-items: center; justify-content: left;",
                      "}\n",
                      "footer p {\n",
                      "\tpadding-left: 50px;\n",
                      "}\n\n"
                      ])

        # # Animation Stuff for later
        # f.writelines(["h1 {\n", 
        #               "\tbackground-color: #002ba1;\n", 
        #               f"\tcolor: {bgColor};\n", 
        #               "\tmargin: 20px auto;\n", 
        #               "\twidth: fit-content;\n", 
        #               "\tpadding: 20px 70px;\n", 
        #               "\tborder-radius: 20px;\n", 
        #               "\tanimation-name: slideDown;\n", 
        #               "\tanimation-duration: 5s;\n", 
        #               "}\n\n"])
        # # .hobbies styles
        # f.writelines([".hobbies h2, .hobbies p, .hobbies ul {\n", 
        #               "\tmargin: 20px auto;\n", 
        #               "\twidth: fit-content;\n", 
        #               "}\n\n"])
        # # keyframes
        # f.writelines(["@keyframes slideDown {\n", 
        #               "\tfrom {\n", 
        #               "\t\tmargin: -70px auto;\n",
        #               "\t } \n"
        #               "\to {\n", 
        #               "\t\tmargin: 20px auto;\n",
        #               "\t } \n"
        #               "}\n\n"])