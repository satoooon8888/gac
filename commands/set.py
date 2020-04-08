import argparse
from account import Accounts, Account
from accounts_stream import AccountsStream
from git_config_stream import GitConfigStream
from const_setting import accounts_json_path
from utils import CommandFailedError
import logger


def cmd_set(args: argparse.Namespace) -> None:
	accounts_stream: AccountsStream = AccountsStream(accounts_json_path)
	accounts: Accounts = accounts_stream.load()
	name: str = args.name
	if not accounts.exist(name):
		logger.error("Not found that name account.")
		raise CommandFailedError()
	account: Account = accounts.find_account(name)
	git_stream: GitConfigStream = GitConfigStream()
	git_stream.set("user.name", account.name)
	git_stream.set("user.email", account.email)
	logger.info("Set successfully")
