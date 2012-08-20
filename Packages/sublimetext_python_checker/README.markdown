# Python PEP-8 and PyFlakes checker for SublimeText 2 editor

This project is a plugin for [SublimeText 2](http://www.sublimetext.com/2) text editor.
It checks all python files you opening and editing through two popular Python checkers - [pep8](http://pypi.python.org/pypi/pep8)
and [PyFlakes](http://pypi.python.org/pypi/pyflakes).

## Installation

Go to your Packages dir (Sublime Text 2 -> Preferences -> Browse Packages). Clone this repository into Packages subdirectory:

    git clone git://github.com/vorushin/sublimetext_python_checker.git

Go to sublimetext_python_checker/ and create file local_settings.py with list of your preferred checkers:

    CHECKERS = [('/Users/vorushin/.virtualenvs/checkers/bin/pep8', []),
                ('/Users/vorushin/.virtualenvs/checkers/bin/pyflakes', [])]

First parameter is path to command, second - optional list of arguments. If you want to disable line length checking in pep8, set second parameter to ['--ignore=E501'].

Restart SublimeText 2 and open some *.py file to see check results. You can see additional information in python console of your editor (go View -> Show Console).

## Why not sublimelint

Before creating this project I used [sublimelint](https://github.com/lunixbochs/sublimelint), which is multilanguage
checker/linter. I described pros and cons of both below.

### sublimelint
- can't use your Python version or your virtualenv
- don't check with pep8
- do checks on every edit
- do checks for Python (derivative of pyflakes), PHP, Perl, Ruby
- works on Windows/Linux/MacOSX

### sublimetext_python_checker
- can use your version of Python and your virtualenv
- do checks only on opening and saving files
- works only on Linux and Mac OS X
- checks only Python files
- checks with pep8 and pyflakes
- all this in a few screens of code
