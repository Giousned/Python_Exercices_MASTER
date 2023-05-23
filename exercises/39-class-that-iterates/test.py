import pytest, io, sys, json, mock, re, os


@pytest.mark.it('The function putNumbers must exist')
def test_function_existence(capsys, app):
    assert app.putNumbers


# @pytest.mark.it('The function should return the expected output')
# def test_expected_output(capsys, app):
#     assert app.putNumbers(100) ==  "0 7 14 21 28 35 42 49 56 63 70 77 84 91 98"

# @pytest.mark.it('The solution should work with other entries')
# def test_another_output(capsys, app):
#     assert app.putNumbers(300) ==  "0 7 14 21 28 35 42 49 56 63 70 77 84 91 98 105 112 119 126 133 140 147 154 161"

