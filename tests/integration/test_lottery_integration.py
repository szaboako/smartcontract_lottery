from brownie import network
import pytest
import time
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, fund_with_link
from scripts.deploy_lottery import deploy_lottery


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()+1000})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()+1000})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(300)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
