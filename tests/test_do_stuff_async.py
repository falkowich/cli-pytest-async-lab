import do_stuff_async
import pytest
# test isolated function
@pytest.mark.asyncio
async def test_main_set_bar():
    assert await do_stuff_async.set_bar("bar") == "bar"


# test printed output
@pytest.mark.asyncio
async def test_main_get_foo_output(capsys):
    await do_stuff_async.get_foo("foo")
    captured = capsys.readouterr()
    assert captured.out == "foo\n"
