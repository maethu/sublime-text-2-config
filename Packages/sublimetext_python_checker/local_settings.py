'''
First parameter is path to command, second - optional list of arguments.
If you want to disable line length checking in pep8, set second parameter
to ['--ignore=E501']. Look at output of pep8 --help for more options.
'''


CHECKERS = [('bin/pep8', []),
            ('bin/pyflakes', [])]
