# markb

Render a markdown file and display it instantly in a browser.

This is a little script that renders a markdown file to a temporary file and
opens a browser to view it. It was originally intended to quickly look at
README files from cool cloned GitHub repositories.

    # attempt to use any file starting with README
    markb

    -- OR --

    # invoke on a given file
    markb post.md

## Development

To develop stuff:

    pip install -e .

Make new release:

    git tag <semver>

Then sdist and all of the magic from here: [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)
