from subprocess import call

# # call(['sudo', 'fuser', '-k', '5435/tcp'])
# call(["docker", "compose" , "down"])
# call(["docker", "compose" , "up" , "-d"])
call(["./manage.py", "makemigrations"])
# call(["./manage.py", "migrate"])
#call(["./manage.py", "runserver"])


#sudo fuser -k 8000/tcp

# docker stop $(docker ps -aq)


# pip install --no-cache-dir -r requirements.txt