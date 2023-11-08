
def on_connect(client):
    pass

def on_disconnect(client):
    pass

def on_recv(client , data):
    print(data.decode())
    pass

def on_send(client , data):
    return data

def cmd_exec(client , cmd , args):
    
    if(cmd == "send"):
        recv_after = False
        if(args[0] == "-cr"):
            recv_after = True
            args = args[1:]

        data = " ".join(args)
        print(f"Sending: {data.encode()}")
        client.send(data.encode())
        if(recv_after):
            client.receive()

    if(cmd == "recv"):
        client.receive()
        

    if(cmd == "disconnect"):
        client.disconnect()    

