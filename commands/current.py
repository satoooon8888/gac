import argparse
from git_config_stream import GitConfigStream
import logger


def cmd_current(args: argparse.Namespace) -> None:
	config_stream: GitConfigStream = GitConfigStream()
	name: str = config_stream.get("user.name")
	email: str = config_stream.get("user.email")
	logger.info("user.name: {}".format(name))
	logger.info("user.email: {}".format(email))
