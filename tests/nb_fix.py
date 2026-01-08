import nbformat
      
nb = nbformat.read("tests/SegSoup_Tutorial.ipynb", as_version=nbformat.NO_CONVERT)
if "widgets" in nb.metadata and "state" not in nb.metadata.widgets:
    nb.metadata["widgets"] = {"state": {}}
nbformat.write(nb, "tests/SegSoup_Tutorial_fix.ipynb")