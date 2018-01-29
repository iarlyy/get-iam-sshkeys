# get-iam-sshkeys
Pull SSH AuthorizedKeys from IAM

#### Create a local user on ec2 called "user_x"
```
useradd user_x
cat /etc/sudoers.d/cloud-init |sed -e 's/ec2-user/user_x/g' > /etc/sudoers.d/user_x
```

#### Create an instance role profile and attach it to your ec2 instance
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListSSHPublicKeys",
                "iam:GetSSHPublicKey",
                "iam:GetGroup"
            ],
            "Resource": "*"
        }
    ]
}
```


#### If the user belongs to group-y and has an active key uploaded, allow login
Append to /etc/ssh/sshd_config
```
Match User user_x
  AuthorizedKeysFile none
  AuthorizedKeysCommand /usr/local/bin/get-iam-sshkeys.py group-y
  AuthorizedKeysCommandUser nobody
```
