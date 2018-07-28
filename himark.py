# oh hi mark!
# hi lisa
#
# Get a markdown file via argument or stdin and output to a tempfile. Open with
# browser. Fun!
# License: WTFPL
from argparse import ArgumentParser
from markdown import markdown
from tempfile import NamedTemporaryFile
import webbrowser


def main():
    parser = ArgumentParser(description="Temporary render markdown files to a "
                                        "temporary file and open in the (your!) browser")
    parser.add_argument("filename", help="A markdown file")
    args = parser.parse_args()

    try:
        with open(args.filename) as md:
            html = markdown(md.read())

        tempfile = NamedTemporaryFile(mode="w+", delete=False)
        tempfile.write(html)

        print("FILE IFLE ILFE", tempfile.name)
        webbrowser.open("file://{}".format(tempfile.name))


    except FileNotFoundError:
        print('File not found "{filename}"'.format(filename=args.filename))


if __name__ == "__main__":
    main()

