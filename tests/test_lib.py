'''
unit tests for a module in the project
run with:
/knot> pytest tests
optional arguments: -vv --html=report.html
'''

from knot.lib import return_true


def test_import():
    assert return_true()
