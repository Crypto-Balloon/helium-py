#!/bin/bash
#
# Run this script to build the necessary docs dir to host github pages.
# Github pages configuration does not support looking in subdirectories.
#

DOCS_BRANCH=docs

if [[ $(git rev-parse --abbrev-ref HEAD) != "$DOCS_BRANCH" ]]; then
    echo "Not safe to run except on $DOCS_BRANCH branch"
    echo "Exiting..."
    exit 1
fi

git reset --hard origin/main
cd docs
make html
rm -rf /tmp/helium-py-docs-html
mv build/html /tmp/helium-py-docs-html
cd ../
rm -rf docs/*
cp -a /tmp/helium-py-docs-html/* docs/
git add docs/
git commit -m "Docs @$(git rev-parse --short HEAD) $(date +'%Y-%m-%d')"
git push origin --force
