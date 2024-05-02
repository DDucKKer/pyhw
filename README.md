# author
[link](https://github.com/DDucKKer)
dduckker

virtualenv
windows:
- python -m venv venv
- .\.venv\Script\activate

linux:
- python -m venv venv
- source venv/bin/activate
------------------------------------------

translation
xgettext -i  .\translation.py -o transl.pot -d this_project
mkdir -p locale\ru\LC_MESSAGES
msginit -i .\transl.pot -o .\locale\ru\LC_MESSAGES\this_project.po -l ru
msgfmt .\locale\ru\LC_MESSAGES\this_project.po -o .\locale\ru\LC_MESSAGES\this_project.mo