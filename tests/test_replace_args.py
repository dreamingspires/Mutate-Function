from signature_replacer import replace_args
import pytest
from copy import copy

@pytest.fixture(
    params=['gentoo', {'replaces': 'gentoo'}], ids=["string", "dict"]
)
async def args_to_replace_simple(request):
    return request.param

@pytest.mark.asyncio
class TestReplaceArgsPos:
    async def test_invalid_no_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func()
        except TypeError as e:
            assert str(e) == 'test_func() missing 1 required positional argument: test'
    async def test_valid_pos_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        assert test_func('test') == {'test': 'test'}
    async def test_valid_keyword_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        assert test_func(test = 'test') == {'test': 'test'}
    async def test_invalid_keyword_body_old_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(gentoo = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() missing 1 required positional argument: test'
    async def test_invalid_keyword_body_random_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() missing 1 required positional argument: test'
    async def test_invalid_too_many_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(1,2,3)
        except TypeError as e:
            assert str(e) == 'test_func() takes 1 positional argument but 3 were given'
    async def test_invalid_multiple_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(2, test=1)
        except TypeError as e:
            assert str(e) == 'test_func() got multiple values for argument \'test\''
    async def test_invalid_keyword_body_keyword_unexpected(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(1, adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''


@pytest.mark.asyncio
class TestReplaceArgsKeyword:
    async def test_valid_no_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo =1):
            return gentoo
        assert test_func() == {'test': 1}
    async def test_valid_pos_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        assert test_func('test') == {'test': 'test'}
    async def test_valid_keyword_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        assert test_func(test = 'test') == {'test': 'test'}
    async def test_invalid_keyword_body_old_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(gentoo = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'gentoo\''
    async def test_invalid_keyword_body_random_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''
    async def test_invalid_too_many_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(1,2,3)
        except TypeError as e:
            assert str(e) == 'test_func() takes 1 positional argument but 3 were given'
    async def test_invalid_too_many_args_one_given(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(*, gentoo =1):
            return gentoo
        try:
            test_func(1)
        except TypeError as e:
            assert str(e) == 'test_func() takes 0 positional arguments but 1 was given'
    async def test_invalid_multiple_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(2, test=1)
        except TypeError as e:
            assert str(e) == 'test_func() got multiple values for argument \'test\''
    async def test_invalid_keyword_body_keyword_unexpected(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(1, adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''


@pytest.mark.asyncio
class TestReplaceArgsPosList:
    async def test_invalid_no_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func()
        except TypeError as e:
            assert str(e) == 'test_func() missing 2 required positional arguments: test and test2'
    async def test_valid_pos_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        assert test_func('rock', 'stone') == {'test': 'rock', 'test2': 'stone'}
    async def test_valid_pos_body_passthrough(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo, rockhopper):
            return [gentoo, rockhopper]
        assert test_func('rock', 'stone', 'pebble') == [{'test': 'stone', 'test2': 'pebble'}, 'rock']
    async def test_valid_pos_body_triple(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple), test3 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        assert test_func('rock', 'stone', 'pebble') == {'test': 'rock', 'test2': 'stone', 'test3': 'pebble'}
    async def test_valid_keyword_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        assert test_func(test = 'rock', test2 = 'stone') == {'test': 'rock', 'test2': 'stone'}
    async def test_invalid_keyword_body_old_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(gentoo = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() missing 2 required positional arguments: test and test2'
    async def test_invalid_keyword_body_random_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() missing 2 required positional arguments: test and test2'
    async def test_invalid_too_many_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(1,2,3)
        except TypeError as e:
            assert str(e) == 'test_func() takes 2 positional arguments but 3 were given'
    async def test_invalid_multiple_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(2, 3, test=1, test2 = 4)
        except TypeError as e:
            assert str(e) == 'test_func() got multiple values for argument \'test\''
    async def test_invalid_keyword_body_keyword_unexpected(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo):
            return gentoo
        try:
            test_func(1, 2, adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''


@pytest.mark.asyncio
class TestReplaceArgsKeywordList:
    async def test_valid_no_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo =1):
            return gentoo
        assert test_func() == {'test': 1, 'test2': 1}
    async def test_valid_pos_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        assert test_func('rock') == {'test':'rock', 'test2': 1}
    async def test_valid_keyword_body(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        assert test_func(test = 'rock') == {'test':'rock', 'test2': 1}
    async def test_invalid_keyword_body_old_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(gentoo = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'gentoo\''
    async def test_invalid_keyword_body_random_keyword(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''
    async def test_invalid_too_many_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(1,2,3)
        except TypeError as e:
            assert str(e) == 'test_func() takes 2 positional arguments but 3 were given'
    async def test_invalid_multiple_args(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(2, test=1)
        except TypeError as e:
            assert str(e) == 'test_func() got multiple values for argument \'test\''
    async def test_invalid_keyword_body_keyword_unexpected(self, args_to_replace_simple):
        @replace_args(test = copy(args_to_replace_simple), test2 = copy(args_to_replace_simple))
        def test_func(gentoo = 1):
            return gentoo
        try:
            test_func(1, adelie = 'test')
        except TypeError as e:
            assert str(e) == 'test_func() got an unexpected keyword argument \'adelie\''

@pytest.mark.asyncio
class TestReplaceArgsRogueErrors:
    async def test_invalid_body_large_number_missing(self):
        @replace_args(test = 'gentoo', test2 = 'gentoo')
        def test_func(gentoo, emporer, rockhopper):
            return gentoo
        try:
            test_func()
        except TypeError as e:
            assert str(e) == 'test_func() missing 4 required positional arguments: emporer, rockhopper, test and test2'

    async def test_invalid_body_large_number_missing_multiple_added(self):
        @replace_args(test = 'gentoo', test2 = 'gentoo')
        def test_func(gentoo, emporer, rockhopper):
            return gentoo
        try:
            test_func()
        except TypeError as e:
            assert str(e) == 'test_func() missing 4 required positional arguments: emporer, rockhopper, test and test2'

    async def test_invalid_body_no_args_some_supplied(self):
        @replace_args()
        def test_func():
            pass
        try:
            test_func('test')
        except TypeError as e:
            assert str(e) == 'test_func() takes 0 positional arguments but 1 was given'

    async def test_invalid_body_no_args_multiple_overwritten(self):
        @replace_args(adelie = {'replaces': 'gentoo', 'default': 3}, emporer = {'replaces': 'gentoo', 'default': 4})
        def test_func(gentoo, rockhopper = 2):
            return [gentoo, rockhopper]
        assert test_func() == [{'adelie': 3,'emporer': 4},2]

    async def test_invalid_body_one_arg_crazy_overwritten(self):
        @replace_args(
            adelie = {'replaces': 'gentoo', 'default': 3},
            emporer = {'replaces': 'gentoo', 'default': 4},
            little = {'replaces': 'king', 'default': 3},
            african = {'replaces': 'king', 'default': 4}
        )
        def test_func(gentoo, rockhopper =2, king =1):
            return [gentoo, rockhopper, king]
        assert test_func(african= 8) == [{'adelie': 3, 'emporer': 4}, 2, {'little': 3, 'african': 8}]

    async def test_invalid_body_one_arg_crazy_overwritten_async(self):
        @replace_args(
            adelie = {'replaces': 'gentoo', 'default': 3},
            emporer = {'replaces': 'gentoo', 'default': 4},
            little = {'replaces': 'king', 'default': 3},
            african = {'replaces': 'king', 'default': 4}
        )
        async def test_func(gentoo, rockhopper =2, king =1):
            return [gentoo, rockhopper, king]
        assert await test_func(african= 8) == [{'adelie': 3, 'emporer': 4}, 2, {'little': 3, 'african': 8}]

    async def test_invalid_body_no_args_one_missing(self):
        @replace_args(
            adelie = {'replaces': 'gentoo'},
            emporer = {'replaces': 'gentoo', 'default': 4},
            little = {'replaces': 'king', 'default': 3},
            african = {'replaces': 'king', 'default': 4}
        )
        def test_func(gentoo, rockhopper =2, king =1):
            return [gentoo, rockhopper, king]
        try:
            test_func(african= 8)
        except TypeError as e:
            assert str(e) == 'test_func() missing 1 required positional argument: adelie'

    async def test_invalid_body_no_args_replaces_missing(self):
        try:
            @replace_args(
                adelie = {}
            )
            def test_func(gentoo, rockhopper =2, king =1):
                return [gentoo, rockhopper, king]
        except ValueError as e:
            assert str(e) == '\'replaces\' missing for adelie'
