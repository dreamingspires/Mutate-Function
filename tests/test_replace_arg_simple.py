from mutate_function import replace_arg_simple
import pytest

@pytest.mark.asyncio
class TestReplaceArgSimple:
    async def test_replace_arg_simple(self):
        @replace_arg_simple('new', 'old')
        def test_func(old):
            return old
        assert test_func(new = 1) == 1
