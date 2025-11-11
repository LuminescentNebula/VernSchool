import subprocess
import os
from pathlib import Path,PosixPath
from pprint import pprint
import sys
from playwright.sync_api import sync_playwright

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
        "--log-level=WARN",
        "--WebPDFExporter.paginate=False"
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


def all_change_extension():
    files = [p for p in root_path.rglob('*.py') if 'Теория' in p.parts]
    pprint(files)
    for file in files:
        change_extension(file, "txt")    

def change_extension(path: Path, to:str):
    new_path_parts = ('Релиз',) + path.parts
    new_path = Path(*new_path_parts)
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path = new_path.with_suffix("."+ to)
    print('"'+str(path)+'"', '".\\'+str(new_path)+'"')
    if isinstance(new_path, PosixPath):
        os.system(" ".join(["cp",'"'+str(path)+'"', '"'+str(new_path)+'"']))
    else:
        os.system(" ".join(["copy",'"'+str(path)+'"', '"'+str(new_path)+'"']))

def all_convert_drawio():
    files = [p for p in root_path.rglob('*.drawio') if 'Теория' in p.parts]
    pprint(files)
    for file in files:
        convert_drawio(file)    

def convert_drawio(path: Path):
    pass

def all_html():
    files = [p for p in root_path.rglob('*.html') if ('Теория' in p.parts) and ('Релиз' not in p.parts)]
    pprint(files)
    for file in files:
        copy_html(file)  
        convert_html_to_pdf(file)

def copy_html(path: Path):
    new_path_parts = ('Релиз',) + path.parts
    new_path = Path(*new_path_parts)
    new_path.parent.mkdir(parents=True, exist_ok=True)
    print('"'+str(path)+'"', '"'+str(new_path)+'"')
    if isinstance(new_path, PosixPath):
        os.system(" ".join(["cp",'"'+str(path)+'"', '"'+str(new_path)+'"']))
    else:
        os.system(" ".join(["copy",'"'+str(path)+'"', '"'+str(new_path)+'"']))

def convert_html_to_pdf(path: Path):
    new_path_parts = ('Релиз',) + path.parts
    new_path = Path(*new_path_parts)
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path = new_path.with_suffix(".pdf")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{path.absolute()}", wait_until="networkidle")
        # Получаем высоту содержимого страницы
        height = page.evaluate("() => document.documentElement.scrollHeight")
        
        # Генерируем PDF с высотой всей страницы (без разрывов)
        page.pdf(
            path=".\\"+str(new_path),
            width="210mm",               # можно задать нужную ширину
            height=f"{height}px",
            print_background=True,
            margin={"top": "0px", "bottom": "0px", "left": "0px", "right": "0px"}
        )
        browser.close()
    print("Converted to", new_path)


all_convert_ipynb_to_pdf()
all_change_extension()
#all_convert_drawio()
all_html()