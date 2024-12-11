import nbformat as nbf
from pathlib import Path
from fire import Fire
def remove_input(fn):
    
    nb = nbf.read(fn, nbf.NO_CONVERT)
    for cell in nb.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        if not 'remove_input' in cell_tags:
            cell_tags.append('remove_input')
            cell['metadata']['tags'] = cell_tags
    nbf.write(nb, fn)

if __name__ == '__main__':
    Fire(remove_input)