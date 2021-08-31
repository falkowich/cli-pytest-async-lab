import do_stuff
import os

# test isolated function
def test_main_set_bar():
    assert do_stuff.set_bar("bar") == "bar"


# pytest input arguments (python -m pytest --switch foo)
def test_args_foo(switch):
    assert switch == "foo"


# test printed output
def test_main_get_foo_output(capsys):
    output = do_stuff.get_foo("foo")
    captured = capsys.readouterr()
    assert captured.out == "foo\n"


def test_main_help_output(capsys):
    os.sys.argv = ["--help"]
    res = do_stuff.main()
    captured = capsys.readouterr()
    assert captured.out == 0
