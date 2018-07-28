from markdown import markdown


with open("input.md") as md:
    html = markdown(md.read())

with open("output.html", "w") as out:
    out.write(html)
