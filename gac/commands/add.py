import argparse
from gac.const_setting import accounts_json_path
from gac.account import Accounts, Account
from gac.accounts_stream import AccountsStream
from gac.utils import CommandFailedError
from gac import logger


def cmd_add(args: argparse.Namespace) -> None:
	stream: AccountsStream = AccountsStream(accounts_json_path)
	accounts: Accounts = stream.load()
	name: str = input("git user.name: ")
	if accounts.exist(name):
		logger.error("This name is already used")
		raise CommandFailedError()
	email: str = input("git user.email: ")
	account: Account = Account(name, email)
	accounts.add(account)
	stream.save(accounts)
	logger.info("Saved successfully")
