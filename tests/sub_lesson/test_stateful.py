from hypothesis.stateful import RuleBasedStateMachine, rule
from contracts.sub_lesson import stateful_fuzz_solvable
from boa.test.strategies import strategy


class StatefulFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = stateful_fuzz_solvable.deploy()

    # "Rule" -> Actions, and can have properties/invariants
    # "Invariants" -> Properties that should always hold true

    @rule(new_number=strategy("uint256"))
    def change_number(self, new_number):
        self.contract.change_number(new_number)

    @rule(input=strategy("uint256"))
    def input_number_returns_itself(self, input):
        response = self.contract.always_returns_input_number(input)
        assert response == input, f"Expected {input}, but got {response}"


TestStatefulFuzzing = StatefulFuzzer.TestCase
