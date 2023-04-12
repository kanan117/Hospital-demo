from datetime import date
from subprocess import call

today = date.today().strftime("%d-%m-%Y")
commit_message = f"Changes made on {today}"

call(["sudo", "git", "add", "."])
call(["sudo", "git", "commit", "-m", commit_message])
call(["git", "push"])
