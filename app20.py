import os
def run_git_commands():
    commands = [
        "git status",
        "git branches"
    ]

    for command in commands:
        print(f"Running command: {command}")
        os.system(command)

run_git_commands()
