import mock, pytest, io, sys 


@pytest.mark.it('The function uppers_and_lowers must exist')
def test_function_existence(capsys, app):
    assert app.uppers_and_lowers


@pytest.mark.it('The function should return the expected output')
def test_output(capsys, app):
    app.uppers_and_lowers("Hello world!") == "UPPER CASE 1 LOWER CASE 9"

@pytest.mark.it('The solution should work with other parameters')
def test_another_entry(capsys, app):
    assert app.uppers_and_lowers("MY Name Is PepE and I LIVE iN thE NexT apartMent") == "UPPER CASE 16 LOWER CASE 22"