#! /bin/bash

# python cookbook/cookbook.py | pandoc --template=tufte.tex --toc-depth=2 --chapters --from=markdown -t latex -o "$1" --toc
python cookbook/cookbook.py | pandoc --toc-depth=2 --chapters --from=markdown -t latex -o "$1" --toc
