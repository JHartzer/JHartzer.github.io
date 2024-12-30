---
layout: post
title: Latex SVG Preprocessor
author: Jacob Hartzer
thumbnail:
date: 2023-12-12
description:
tags: tex
categories:
---

As part of my [tex](https://tug.org/) work process, I like to generate graphics using inkscape SVG files. However, these files must be converted into PDFs for pdflatex to be able to process the figures. Normally, this would be a manual process and therefore quite cumbersome if there are multiple rounds of tweaks in inkscape to update typesetting in tex. To automate this process, I wrote a simple preprocessor script that checks for changes in the SVG hash and, if changes are found, will regenerate a PDF using the inkscape command line interface. The script is available as a [gist](https://gist.github.com/JHartzer/a3cc3cb276f343d7bd145ab50cdd9dab) or is copied below:


```python
import hashlib
import os
import subprocess

def hash_file(file_path):
    CHUNK_SIZE = 2**16
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(CHUNK_SIZE)
    return file_hash.hexdigest()


fig_dir = os.path.dirname(os.path.abspath(__file__))
for path, _, files in os.walk(fig_dir):
    for file_name in files:
        if file_name.endswith('.svg'):
            svg_path = os.path.join(path, file_name)
            pdf_path = svg_path.replace('.svg', '.pdf')
            hash_path = svg_path.replace('.svg', '.hash')
            svg_hash = hash_file(svg_path)

            generate_pdf = True
            if os.path.isfile(pdf_path):
                if os.path.isfile(hash_path):
                    with open(hash_path, 'r') as f:
                        old_hash = f.readline()
                        generate_pdf = (old_hash != svg_hash)
                else:
                    with open(hash_path, 'w') as f:
                        f.write(svg_hash)
                        generate_pdf = True

            if (generate_pdf):
                subprocess.run([
                    'inkscape',
                    svg_path,
                    '--export-area-drawing',
                    '--batch-process',
                    '--export-type=pdf',
                    f'--export-filename={pdf_path}'
                ],
                    capture_output=True, text=True)
```