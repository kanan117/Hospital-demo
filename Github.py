from subprocess import call

call(["sudo", "git", "add", "."])
call(["sudo", "git", "commit", "-m" , """KNN"""])
call(["sudo", "git", "push"])


