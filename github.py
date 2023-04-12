from subprocess import call

call(["sudo", "git", "add", "."])
call(["sudo", "git", "commit", "-m" , """test.py"""])
call(["git", "push"])


