from subprocess import call



call(["docker", "compose" , "down"])
call(["docker", "compose" , "up" , "-d"])
call(["./manage.py", "makemigrations"])
call(["./manage.py", "migrate"])
call(["./manage.py", "runserver"])


