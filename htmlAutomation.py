#!/usr/bin/env python3

import os

project_name = input("Name of Project: ")

if os.path.isdir(project_name):
    print('Project Already Exists')
    quit()
else:
    os.mkdir(project_name)
    print('Successfully Created Empty Project')

os.chdir(project_name)
os.mkdir('images')
os.mkdir('videos')

htmlContent = '<html>\n\t<head>\n\t\t<title> ' + project_name + ' </title>\n\t\t<link rel="stylesheet" type="text/css" href="style.css">\n\t</head>\n<body>\n\t<p id="label"></p>\n\t<button id="btn" onclick="showText()"> Click Me </button>\n\t<script src="script.js"></script>\n</body>\n</html>'

htmlFile = open('index.html', 'w')
htmlFile.write(htmlContent)
htmlFile.close()

cssContent = '* {\n\tmargin:0;\n\tpadding:0;\n}\nbody {\n\theight:100vh;\n\tdisplay:flex;\n\tjustify-content:center;\n\talign-items:center;\n}\n#btn {\n\twidth:200px;\n\tpadding: 20px 10px;\n\tborder-radius:5px;\n\tbackground-color:red;\n\tcolor:#fff;\n\toutline:none;border:none;\n}\np {\n\tfont-size:30px;\n}'

cssFile = open('style.css', 'w')
cssFile.write(cssContent)
cssFile.close

jsContent = 'function showText() {\n\tdocument.getElementById("label").innerHTML="Successfully Created Project";\n\tdocument.getElementById("btn").style="background-color:green;"\n}'

jsFile = open('script.js', 'w')
jsFile.write(jsContent)
jsFile.close()




