import nbformat

# Cargar el notebook
nb = nbformat.read("tests/SegSoup_Tutorial.ipynb", as_version=4)

# Limpiar metadatos de widgets
if 'widgets' in nb.metadata:
    del nb.metadata['widgets']

# Guardar de nuevo
nbformat.write(nb, "tests/SegSoup_Tutorial_fix.ipynb")