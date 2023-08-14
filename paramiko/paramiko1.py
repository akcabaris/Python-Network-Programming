import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = "10.10.10.21"
portSSH = 22
usernameSSH = 'msfadmin'
passwordSSH = 'msfadmin'
ssh.connect(ip, port=portSSH, username=usernameSSH, password=passwordSSH)

command = "whoami"

stdin, stdout, stderr = ssh.exec_command(command)
cmd_output = stdout.read()

print(cmd_output.decode())