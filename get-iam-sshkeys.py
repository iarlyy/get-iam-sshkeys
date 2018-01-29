#!/usr/bin/env python3
import sys

import boto3

iam_client = boto3.client("iam")
users = iam_client.get_group(GroupName=sys.argv[1])['Users']

for u in users:
    user_keys = iam_client.list_ssh_public_keys(UserName=u['UserName'])['SSHPublicKeys']
    for k in user_keys:
        if k['Status'] == 'Active':
            key = iam_client.get_ssh_public_key(UserName=u['UserName'], SSHPublicKeyId=k['SSHPublicKeyId'], Encoding='SSH')['SSHPublicKey']['SSHPublicKeyBody']
            print('#{}\n{}'.format(u['UserName'], key))
