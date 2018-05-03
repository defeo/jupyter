import jinja2, nbformat
from nbconvert import HTMLExporter
from pathlib import Path
from distutils.dir_util import copy_tree
import config

def copy_assets():
    copy_tree('src/assets', config.OUTPUT_DIR + '/assets')

def generate_notebooks():
    exporter = HTMLExporter(
        extra_loaders=[jinja2.FileSystemLoader('src/templates')])
    exporter.template_file = 'notebook.jinja'
    
    notebooks = []
    dir = Path(config.OUTPUT_DIR) / config.NOTEBOOK_DIR
    dir.mkdir(parents=True, exist_ok=True)
    for nb in Path(config.NOTEBOOK_DIR).glob('*.ipynb'):
        with nb.open() as f:
            html, meta = exporter.from_file(f, resources={
                "filename": nb.name,
                })
            path = dir / (nb.stem + '.html')
            path.write_text(html)
            notebooks.append({
                'url'  : path.relative_to('build'),
                'name' : nb.name,
                })
    return notebooks

def generate_index(notebooks):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('src/templates'),
        autoescape=True)
    tpl = env.get_template('index.jinja')
    out = tpl.render(notebooks=notebooks,config=config)
    (Path(config.OUTPUT_DIR) / 'index.html').write_text(out)
    
if __name__ == '__main__':
    copy_assets()
    nbs = generate_notebooks()
    generate_index(nbs)
    
