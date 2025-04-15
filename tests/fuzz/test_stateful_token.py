from hypothesis.stateful import RuleBasedStateMachine, rule
from contracts import snek_token
from boa.test.strategies import strategy


class StatefulTokenFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.initial_supply = 0
        self.contract = None

    @rule(initial_supply=strategy("uint256"))
    def deploy_contract(self, initial_supply):
        if self.contract is None:
            self.initial_supply = initial_supply
            self.contract = snek_token.deploy(initial_supply)
            assert self.contract.totalSupply() == initial_supply

    def mint_more(self):
        if self.contract is not None:
            self.contract.super_mint()
            assert self.contract.totalSupply() > self.initial_supply


TestTokenStateful = StatefulTokenFuzzer.TestCase
