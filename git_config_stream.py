from typing import Literal
import subprocess

GitConfigLocation = Literal["global", "system", "local", "worktree"]


class GitConfigStream:
	def __init__(self, location: GitConfigLocation = "global"):
		self.location: GitConfigLocation = location

	def get(self, key: str) -> str:
		command = ["git", "config", "--{}".format(self.location), key]
		proc: subprocess.CompletedProcess = subprocess.run(
			command,
			shell=True,
			stdout=subprocess.PIPE
		)
		return proc.stdout.decode().rstrip()

	def set(self, key: str, value: str) -> None:
		command = ["git", "config", "--{}".format(self.location), key, value]
		subprocess.run(command, shell=True)
