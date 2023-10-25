import paramiko

ssh_hosts = [
    {"url": "yand.dyndns.org", "port": 1922, "user": "student"},
    {"url": "95.165.133.145", "port": 1922, "user": "student"},
]
for ssh_host in ssh_hosts:
    host_url = ssh_host["url"]
    host_port = ssh_host["port"]
    host_user = ssh_host["user"]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host_url, username=host_user, password='Pa$$w0rd', port=host_port)
    stdin, stdout, stderr = client.exec_command('ls /etc/python3')
    if "No such file or directory" in stderr.read().decode():
        print(f"Файл /etc/python3 не найден на хосте {host_url}")
    else:
        print(f"Файл /etc/python3 найден на хосте {host_url}")
    client.close()
    stdin.close()