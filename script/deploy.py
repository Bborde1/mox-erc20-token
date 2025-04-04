from contracts import snek_token
from eth_utils import to_wei

INITIAL_SUPPLY = to_wei(1000, "ether")


def deploy():
    snek_contract = snek_token.deploy(INITIAL_SUPPLY)
    print(f"Deployed to {snek_contract.address}")


def moccasin_main():
    return deploy()
