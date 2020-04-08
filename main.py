import argparse
from commands.current import cmd_current
from commands.set import cmd_set
from commands.add import cmd_add
from commands.list import cmd_list
from commands.delete import cmd_delete
from account import Accounts
from accounts_stream import AccountsStream
from utils import CommandFailedError
from const_setting import accounts_json_path
import logger
import sys
import os

"""
gac current
gac set
gac add
gac list
"""


def generate_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser()
	sub_parser = parser.add_subparsers()
	# current
	current_parser = sub_parser.add_parser("current")
	current_parser.set_defaults(handler=cmd_current)
	# set
	set_parser = sub_parser.add_parser("set")
	set_parser.add_argument("name", type=str)
	set_parser.set_defaults(handler=cmd_set)
	# add
	add_parser = sub_parser.add_parser("add")
	add_parser.set_defaults(handler=cmd_add)
	# add
	delete_parser = sub_parser.add_parser("delete")
	delete_parser.add_argument("name", type=str)
	delete_parser.set_defaults(handler=cmd_delete)
	# list
	list_parser = sub_parser.add_parser("list")
	list_parser.set_defaults(handler=cmd_list)
	return parser


def init() -> None:
	if not os.path.exists(accounts_json_path):
		logger.warning("Can't Find accounts.json. Create it")
		stream: AccountsStream = AccountsStream(accounts_json_path)
		stream.save(Accounts())


def main() -> None:
	parser: argparse.ArgumentParser = generate_parser()
	args: argparse.Namespace = parser.parse_args()
	init()

	if hasattr(args, 'handler'):
		# intellijで何故かargs.handlerがstrとされる
		try:
			# noinspection PyCallingNonCallable
			args.handler(args)
		except CommandFailedError:
			sys.exit(1)
		else:
			sys.exit(0)
	else:
		logger.error("Undefined command")
		parser.print_help()
		sys.exit(1)


if __name__ == "__main__":
	main()
