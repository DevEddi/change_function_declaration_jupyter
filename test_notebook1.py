from testbook import testbook

import pytest

@testbook('./notebook_1.ipynb', execute= 0)
def test_output(tb):
    assert tb.cell_output_text(0) == 'Hello World!'

@testbook('./notebook_1.ipynb', execute= 1)
def test_add(tb):
    add = tb.ref('add')
    assert add(1, 2) == 3