import argparse
from gac.const_setting import accounts_json_path
from gac.account import Accounts
from gac.accounts_stream import AccountsStream
from gac.utils import CommandFailedError
from gac import logger


def cmd_delete(args: argparse.Namespace) -> None:
	stream: AccountsStream = AccountsStream(accounts_json_path)
	accounts: Accounts = stream.load()
	name = args.name
	if not accounts.exist(name):
		logger.error("Not found that name account.")
		raise CommandFailedError()
	accounts.delete(name)
	stream.save(accounts)
	logger.info("Deleted successfully")
