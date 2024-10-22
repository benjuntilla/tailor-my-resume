#!/usr/bin/env bash

# Run tailor script in container
guix shell -C -F -N openssl node poetry coreutils gcc-toolchain git -D ungoogled-chromium --share=/home/ben --preserve='^DISPLAY$' --preserve='^XAUTHORITY$' -- ./crawl-and-prompt.sh

# Copy the contents of prompt.txt to the clipboard
echo "Copied prompt.txt to clipboard"
cat prompt.txt | wl-copy

# Open Firefox
firefox https://claude.ai &

# Prompt the user for YAML input
echo "Please enter the YAML-formatted output from Claude (press Ctrl+D when finished):"
yaml_input=$(cat)

# Save the YAML input to tailored.yaml
echo "$yaml_input" > tailored.yaml

echo "YAML input has been saved to tailored.yaml"

# render and open
if rendercv render -use pdflatex tailored.yaml; then
    zathura "$(ls -t rendercv_output/*.pdf | head -n 1)"
fi
