# SSH Login with Aliases

Tired of logging into servers by copying and pasting IPs and passwords everytime?

Use this command to login seamlessly into your server by as simply as providing the alias:

```
imlogin my-server
```

```
Logging to 03.01.200.900 with user: satoshi ...

Last login: Sat Jan 03 11:45:00 2009 from 04.01.202.200
[satoshi@my-server ~]$ 
```

## Requirements

- jq. Install with `sudo apt-get install jq`
- sshpass. Install with `sudo apt-get install sshpass`

## Instructions

1. Copy the `imlogin()` function in [imlogin.sh](https://github.com/paras-lehana/utils/blob/master/linux/bash/login/imlogin.sh) file and paste it into your ~/.bashrc or bash_aliases or bash_functions.
2. In the `imlogin()` function, there is a `CONFIG_FILE` constant that determines the path of the credentials file ip-cred.json. Change the path if required.
3. Make a file named ip-cred.json in the path given in `CONFIG_FILE`. A sample [file](https://github.com/paras-lehana/utils/blob/master/linux/bash/login/ip-cred.json) is also provided.
4. Add your login details in the `ip-cred.json` file.
5. Restart your terminal or run `. ~/.bashrc`. 
6. If you are logging into the server for the first time, do normal ssh to your server i.e. `ssh <ip>`.
7. If it asks for adding the IP to known_hosts, allow. Now, you can exit the login and try logging with the imlogin command. 

## Usage

Suppose you have been doing this until you found this script:

```linux
ssh paras@03.01.200.900
paras_65871@35.193.10.136's password: youcantseeme
```

Make a new entry to the `CONFIG_FILE`:

```json
{
    "paras-server": {
        "desc": "Paras Server that houses the internet!",
        "name": "The Mighty Paras Server",
        "ip": "03.01.200.900",
        "cred": {
            "paras": "youcantseeme",
            "admin": "obviouslyadmin"
        },
        "default_user": "paras",
        "env": ["dev", "stg"]
    }
}

```
The details of the entry are:
- **key:** The server alias is now `paras-server` that will be used to login. **Mandatory.**
- **desc:** Description of the server that helps you to differentiate among all the servers. Not Mandatory.
- **name:** Descriptive name of your server or the hostname that can be different from alias. Not Mandatory.
- **ip:** IP of the server. **Mandatory.**
- **cred:** It consists of key-value pairs of the user and their passwords. Used to login with `imlogin <user>@<server-alias>` e.g. `imlogin admin@paras-server`. **One Mandatory.**
- **default_user:** The user to log in if you skip username. Used to login simply with `imlogin <server-alias>` e.g. `imlogin paras-server`. In this case, `paras` will be logged into if it is the `default_user`. Not Mandatory.
- **env:** The environments of the server. I use paras-server for both development and staging. This can be used to put warnings or restrictions for production servers. Not Mandatory

Thus, a simple entry (with mandatory fields) could look like:

```json
{
    "paras-server": {
        "ip": "03.01.200.900",
        "cred": {
            "paras": "youcantseeme",
        }
    }
}

```

If you are logging into the server for the first time, do simple SSH first to add entry into known_hosts:

```
ssh 03.01.200.900

The authenticity of host 'server-hostname-can-be-different-from-server-alias (03.01.200.900)' can't be established.
RSA key fingerprint is [key fingerprint].
Are you sure you want to continue connecting (yes/no)? yes
```

Now, to use the command, the format is `imlogin <username>@<server alias>`:
```
imlogin admin@paras-server
```

You can also skip the username if you want to login with the `default_user` (if given):
```
imlogin paras-server
```

```
Logging to 03.01.200.900 with user: paras ...

Last login: Sat Jan 03 11:45:00 2009 from 04.01.202.200
[paras@server-hostname-can-be-different-from-server-alias ~]$ 
```

If you want the password to be visible in the output of command then you can pass `--show-cred` argument in the command:
```sh
imlogin paras-server --show-cred
```

```
Logging to 03.01.200.900 with credentials paras:youcantseeme ...

Last login: Sat Jan 03 11:45:00 2009 from 04.01.202.200
[paras@server-hostname-can-be-different-from-server-alias ~]$ 
```

Add as many servers and users you want and login with a single and rememberable command! 


