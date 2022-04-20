from brownie import accounts, config, SimpleStorage, network

# import os


def brownie_simple_storage():
    account = get_account( )
    # print(account)
    # account = accounts.load("freecodecamp-account")
    # print(account)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    # This code will return an object which we are storing in the simple_storage variable.
    stored_value = simple_storage.retrieve()
    print(stored_value)
    trans = simple_storage.store(15, {"from": account})
    trans.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)


# Writing a function to find the development network we are working with
def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    brownie_simple_storage()
