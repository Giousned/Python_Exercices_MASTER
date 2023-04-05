import mock, pytest, io, sys 


@pytest.mark.it('The function square_odd_numbers must exist')
def test_function_existence(capsys, app):
    assert app.square_odd_numbers


@pytest.mark.it('The function should return the expected output')
def test_output(capsys, app):
    app.square_odd_numbers("1,2,3,4,5,6,7,8,9") == "1,3,5,7,9"

@pytest.mark.it('The solution should work with other parameters')
def test_another_entry(capsys, app):
    assert app.square_odd_numbers("10,21,32,43,54,65,76,87,98") == "21,43,65,87"