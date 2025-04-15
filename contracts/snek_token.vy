# pragma version 0.4.0
"""
@license MIT
@title snek_token
@author Brandon
@notice This is my first ERC20 token contract, INVARIANT: sender_total should always return the sum of 
"""

from ethereum.ercs import IERC20

implements: IERC20

from snekmate.auth import ownable as ow
from snekmate.tokens import erc20

initializes: ow
initializes: erc20[ownable := ow]

exports: erc20.__interface__

NAME: constant(String[25]) = "snek_token"
SYMBOL: constant(String[5]) = "SNEK"
DECIMALS: constant(uint8) = 18
EIP712_NAME: constant(String[50]) = "snek_token"
EIP712_VERSION: constant(String[20]) = "1"
minters: public(DynArray[address, 1000])
mintAmounts: public(DynArray[uint256, 1000])


@deploy
def __init__(initial_supply: uint256):
    ow.__init__()
    erc20.__init__(NAME, SYMBOL, DECIMALS, EIP712_NAME, EIP712_VERSION)
    erc20._mint(msg.sender, initial_supply)

@external
def super_mint():
    # We forget to update the total supply!
    # self.totalSupply += amount
    amount: uint256 = as_wei_value(100, "ether")
    erc20.totalSupply = erc20.totalSupply + amount
    erc20.balanceOf[msg.sender] = erc20.balanceOf[msg.sender] + amount
    self.minters.append(msg.sender)
    self.mintAmounts.append(amount)
    log IERC20.Transfer(empty(address), msg.sender, amount)

@external
def get_minters() -> DynArray[address, 1000]:
    """
    @notice Returns list of minters of this token
    """
    return self.minters
