from contracts import snek_token
from hypothesis import given
from boa.test.strategies import strategy


@given(input=strategy("uint256"))
def test_initial_supply(input):
    token_contract = snek_token.deploy(input)
    assert token_contract.totalSupply() == input
