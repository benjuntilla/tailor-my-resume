# tailor my resume!

## how it works
- pull MD-formatted JD with `crawl4ai`
- Construct prompt using MD-formatted JD and YAML-formatted resume
- render `tailored.yaml` with `rendercv` 

## system dependencies (outside of what's in `pyproject.toml`)
- poetry
- rendercv
- wl-copy (i guess it doesn't have to be wayland-specific but whatever)

## installation
`poetry install`

## usage
`./tailor.sh`

