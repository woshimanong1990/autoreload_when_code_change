# coding:utf-8
import os
import sys
import time
import subprocess
auto_reload = os.environ.get("auto_reload", False)
if auto_reload:
    import source_code_monitor as monitor
    monitor.start()
else:
    # will stop here
    while True:
        args = [sys.executable] + sys.argv
        os.environ['auto_reload'] = "True"
        p = subprocess.Popen(args)
        # todo: may use return code, ref django
        while p.poll() is None:
            time.sleep(1)


# your real code here
def main():
    pass


if __name__ == "__main__":
    main()
