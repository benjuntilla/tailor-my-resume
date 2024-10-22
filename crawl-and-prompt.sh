#!/usr/bin/env bash

echo "RUNNING CRAWLER"
poetry run python crawl.py;
echo

echo "CRAWLER OUTPUT:"
echo $(cat output.md)
echo

echo "GENERATING PROMPT AND SAVING TO prompt.txt"
echo "<JOB DESCRIPTION>
$(cat output.md)
</JOB DESCRIPTION>

<RESUME TEMPLATE>
$(cat $HOME/src/resume/src/base.yaml)
</RESUME TEMPLATE>

<PROMPT>
Tailor the provided resume in YAML format to the MD-formatted webpage with the job description. Determine desired skills and keywords, and ensure that they are emphasized in the tailored resume. Be sure to use double asterisks to bold words. And most importantly, make sure your output is valid YAML.
</PROMPT>" > prompt.txt
echo
