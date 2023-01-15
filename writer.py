

# write scores to index.html file
def write_to_index_html_file(scoreboard):
    header = "<!DOCTYPE html> <html> <body> <h1>Scoreboard 2023</h1>"
    body = "<ul>"   

    for ti_gars in scoreboard:
        body += "<li>" + ti_gars[0] + ": " + str(ti_gars[1]) + "</li>" + "\n"
    
    body += "</ul>"
    footer = "</body> </html>"
    text = header + body + footer
    f = open("index.html", "w")
    f.write(text)
    f.close()
    
