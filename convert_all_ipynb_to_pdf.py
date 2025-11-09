import subprocess
import os
from pathlib import Path
from pprint import pprint

root_path = Path('.')

jn_command = [
        "jupyter",
        "nbconvert",
        None,
        "--to", 
        "webpdf", 
        "--allow-chromium-download",
        "--output-dir", 
        None,
        "--log-level=WARN"
    ]

def all_convert_ipynb_to_pdf():
    # Find all .ipynb files in Теория folders
    notebooks = [p for p in root_path.rglob('*.ipynb') if 'Теория' in p.parts]
    pprint(notebooks)
    # Convert all found notebooks
    failed=[]
    for nb in notebooks:
        try:
            convert_ipynb_to_pdf(nb)    
        except KeyboardInterrupt:
            break
        except:
            print("NOT CONVERTED:", nb)
            failed.append(nb)
    print("NOT CONVERTED:", failed)

def convert_ipynb_to_pdf(ipynb_path: Path):
    new_path_parts = ('Релиз',) + ipynb_path.parts
    pdf_path = Path(*new_path_parts[:-1])
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    jn_command[2] = str(ipynb_path).replace("\\","/")
    jn_command[7] = pdf_path

    subprocess.run(jn_command,check=True)

    print(f'Converted "{ipynb_path}" to "{pdf_path}"')


def all_convert_py_to_txt():
    files = [p for p in root_path.rglob('*.py') if 'Теория' in p.parts]
    pprint(files)
    for nb in files:
        convert_py_to_txt(nb)    

def convert_py_to_txt(path: Path):
    new_path_parts = ('Релиз',) + path.parts
    new_path = Path(*new_path_parts)
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path = new_path.with_suffix(".txt")
    print('"'+str(path)+'"', '".\\'+str(new_path)+'"')
    os.system(" ".join(["copy",'"'+str(path)+'"', '"'+str(new_path)+'"']))

#all_convert_ipynb_to_pdf()
all_convert_py_to_txt()