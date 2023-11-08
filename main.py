import client
import sys
import time
import handler
from importlib import reload

if __name__ ==  "__main__":
    
    #parse host and port from command line
    host = sys.argv[1]
    port = 8000
    if(":" in host):
        port = int(host.split(":")[1])
        host = host.split(":")[0]

    cli = client.client()
    print(f"Connecting to {host}:{port}")

    con_start_time = time.time()
    cli.connect((host , port))
    con_suc_time = time.time()
    print(f"Connected in {con_suc_time-con_start_time} sec(s)")

    while(1):
        cmd_line = input(f"@{host}:{port}>")
        reload(handler)
        #simpler args parsing and such
        cmd_data = cmd_line.split(" ")
        cmd = cmd_data[0]
        args = cmd_data[1:]
        handler.cmd_exec(cli , cmd , args)
