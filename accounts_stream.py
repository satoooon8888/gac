from typing import TypedDict, List
from account import Accounts, Account
import json
import os

class AccountJSON(TypedDict):
	name: str
	email: str


AccountsJSON = List[AccountJSON]


def json_to_accounts(accounts_json: AccountsJSON) -> Accounts:
	accounts: Accounts = Accounts()
	for account_json in accounts_json:
		name = account_json["name"]
		email = account_json["email"]
		account: Account = Account(name, email)
		accounts.add(account)
	return accounts


def accounts_to_json(accounts: Accounts) -> AccountsJSON:
	accounts_json: AccountsJSON = []
	for account in accounts:
		account_json: AccountJSON = {"name": account.name, "email": account.email}
		accounts_json.append(account_json)
	return accounts_json


class AccountsStream:
	def __init__(self, path: str) -> None:
		self.path: str = path

	def exist(self) -> bool:
		return os.path.exists(self.path)

	def load(self) -> Accounts:
		with open(self.path, "r") as f:
			accounts_json: AccountsJSON = json.load(f)
		return json_to_accounts(accounts_json)

	def save(self, accounts: Accounts) -> None:
		with open(self.path, "w") as f:
			accounts_json = accounts_to_json(accounts)
			json.dump(accounts_json, f)
