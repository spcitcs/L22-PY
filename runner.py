from datetime import datetime
import os
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    n = 0
    print(f"[ RUNNING - {user} ]")
    for module in os.listdir("."):
        taskDir = os.path.join(module, "tasks", user)
        if(os.path.isdir(module) and os.path.isdir(taskDir)):
            for task in os.listdir(taskDir):
                dir = os.path.join(taskDir, task)
                with open(dir) as f:
                    firstline = f.readlines()[0].rstrip()
                if "--RUN" in firstline:
                    n += 1
                    tag = firstline.split("--RUN")[-1].strip()
                    if(tag != ""):
                        tag = " : " + tag
                    print(f"\n[ TASK - {n}{tag} ]")
                    print(f"[ Running from {dir} ]\n")
                    start = datetime.now()
                    exec(open(dir).read())
                    end = datetime.now()
                    print(f"\n[ Exec Time : {end-start} ]")
    if(n == 0):
        print("[ ERROR ]")
        print("[ No Task with tag --RUN found! ]")
        print("[ Please add --RUN tag to your files to run! ]")
    print("[ FINISHED ]")