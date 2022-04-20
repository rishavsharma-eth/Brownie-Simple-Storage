from brownie import accounts, network


def main():
    # account = accounts[0]
    account = accounts.load("freecodecamp-account")
    print(account)



# with open("compiled_code.json", "w") as file :
#     json.dump(compiled_sol,file)