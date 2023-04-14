from datetime import date
from subprocess import call

today = date.today().strftime("%d-%m-%Y")
x = "doctorcount"
# f"Update {today}"

call(["sudo", "git", "add", "."])
call(["sudo", "git", "commit", "-m", x])
call(["git", "push"])
