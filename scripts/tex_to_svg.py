#!/usr/bin/env python3

import re
import os

with open('example.md', 'r') as file:
    pattern = re.compile(r'<!--\s*\$(.*?)\$:[a-zA-Z0-9_.+-\-]+\.svg-->')
    for line in file:
        for match in pattern.finditer(line):
            tex, fname = match.group().strip('<!--').strip('-->').split(':')
            with open('tmp.tex', 'w+') as tex_out:
                tex_out.write(r'\documentclass{standalone} \begin{document} ')
                tex_out.write(tex)
                tex_out.write(r' \end{document}')

            os.system('pdflatex tmp.tex')
            os.system(f'pdf2svg tmp.pdf {fname}')
            os.remove('tmp.aux')
            os.remove('tmp.log')
            os.remove('tmp.pdf')
            os.remove('tmp.tex')
