#!/bin/bash
$(which python3) -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
echo "# Project \`your-project\`" > README.md
echo -e "*.sqlite3\n.vscode/\n.pylintrc\n.prettierrc" >> .gitignore
rm -rf .git
git init
git add .
git commit -m "initial commit"
code .
rm -- "$0"