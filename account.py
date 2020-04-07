from typing import List, Iterator


class AccountNotFoundError(Exception):
	pass


class AccountNameAlreadyUsedError(Exception):
	pass


class Account:
	def __init__(self, name: str, email: str) -> None:
		self.name: str = name
		self.email: str = email


class Accounts:
	def __init__(self, account_list: List[Account]):
		self.account_list = account_list

	def __iter__(self) -> Iterator[Account]:
		return iter(self.account_list)

	def find_account(self, name: str) -> Account:
		for account in self.account_list:
			if account.name == name:
				return account
		raise AccountNotFoundError()

	def exist(self, name: str) -> bool:
		for account in self.account_list:
			if account.name == name:
				return True
		return False

	def delete(self, name: str) -> None:
		for i, account in enumerate(self.account_list):
			if account.name == name:
				self.account_list.pop(i)
		raise AccountNotFoundError()

	def add(self, account: Account) -> None:
		if self.exist(account.name):
			raise AccountNameAlreadyUsedError()
		else:
			self.account_list.append(account)
