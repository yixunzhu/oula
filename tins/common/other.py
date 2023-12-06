# -*- coding: utf-8 -*-
__author__ = 'zhuyixun'
__time__ = '2023/1/12'

import paramiko


def str_to_list(_str):
    _str_to_list = _str.split()
    return _str_to_list


def bbb():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.3.212', username='root', password='Hello123$')
    cmd1 = 'find /opt/cloudquery -type f -name "*.yml" | grep -v "/\.'
    stdin, stdout, stderr = ssh.exec_command(cmd1)
    output = stdout.read().decode('utf-8')
    # error = stderr.read().decode('utf-8')
    print(output)


def find_files(dir_path, suffix):

    command = f'find {dir_path} -type f -name "*.{suffix}"'
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8').strip()
    if output:
        return output.split('\n')
    else:
        return []




if __name__ == '__main__':
    # Alter Create_schema Create_table Create_index Create_view Create_function Create_procedure  Drop Delete Insert Execute Update Truncate"
    # a="Alter Create_table Create_index Create_view Create_function Create_procedure Drop Delete Insert Execute Update Truncate"
    # a="Alter Create_table Create_index Drop  Delete Insert Update Truncate"
    # a = "Alter Create_table Create_index Drop  Delete Insert Update Truncate"
    # a = "Alter Drop Dblink_operate"
    # print(str_to_list(a))
    # bbb()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='example.com', username='user', password='password')
    ssh.connect(hostname='192.168.3.212', username='root', password='Hello123$')
    files = find_files('/opt/cloudquery', 'yml')
    for file in files:
        print(file)

    ssh.close()
