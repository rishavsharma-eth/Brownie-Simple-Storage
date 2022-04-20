from brownie import SimpleStorage, accounts


# Using this function we are testing that the initial value of the function
# that we are calling should be equal to zero
def test_cont():
# Arrange
    account = accounts[0]
# Acting
    simple_storage = SimpleStorage.deploy({"from": account})
    get_initial = simple_storage.retrieve()
    expected_value = 0
# Asserting
    assert get_initial == expected_value


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()
