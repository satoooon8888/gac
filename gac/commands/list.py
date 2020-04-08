import argparse
from gac.account import Accounts
from gac.accounts_stream import AccountsStream
from gac.const_setting import accounts_json_path
from gac.utils import CommandFailedError
from gac import logger


def cmd_list(args: argparse.Namespace) -> None:
	stream: AccountsStream = AccountsStream(accounts_json_path)
	accounts: Accounts = stream.load()
	if len(accounts) == 0:
		logger.info("Haven't added accounts yet. try \"gac add\"")
		raise CommandFailedError()
	longest_name_length = 0
	for account in accounts:
		longest_name_length = max(longest_name_length, len(account.name))
	longest_name_length += 0
	logger.info("NAME" + " " * (longest_name_length - 4) + " | EMAIL")
	logger.info("-" * (longest_name_length + 8))
	for account in accounts:
		logger.info(account.name + " " * (longest_name_length - len(account.name)) + " | " + account.email)
