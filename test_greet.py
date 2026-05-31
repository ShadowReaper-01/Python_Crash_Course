from Testing_code import greet

def test_Name():
    assert greet('sparsh','gautam') == 'hello , dear sparsh gautam , Welcome Aboard!!'

    assert greet('snoop','dogg') == 'hello, dear snoop dogg , Welcome Aboard!!'