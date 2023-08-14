import paramiko
def sendCommand(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    comment_output = stdout.read()
    print("<<"+comment_output.decode())

ip = "10.10.10.21"
portSSH = 22
usernameSSH = 'msfadmin'
passwordSSH = 'msfadmin'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh.connect(ip, port=portSSH,username=usernameSSH,password=passwordSSH)

command="whoami"

while command.lower().strip()!="quit":
    if command!="":
        sendCommand(command)
    command = input(">>")
