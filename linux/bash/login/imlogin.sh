: '

Function for logging into your servers using aliases.

- You can paste this function in your .bash_aliases, .bash_functions or .bashrc file. They are available in your home directory e.g. ~/.bashrc.
- Requires jq installed. Can be installed on Ubuntu with sudo apt-get install jq.
- Your credential file resides at CONFIG_FILE. Change it as per your preferences. A sample file is also available in this directory or https://github.com/paras-lehana/utils/blob/master/linux/bash/login/ip-cred.json
- Please find instructions in the README or https://github.com/paras-lehana/utils/tree/master/linux/bash/login#readme

'

function imlogin() {

    if [ "$1" = "--help" ]
    then
        echo -e "\n- For logging into Auto-Suggest Servers, use imlogin <user>@<server_alias>.\n- The IP and Credentials for the server are present in CONFIG_FILE.\n- For example, imlogin suggest@dev-suggest logins suggest user into server and with password against dev-suggest alias in CONFIG_FILE.\n- To show CONFIG_FILE, use --config.";
            
        return;
    fi

    CONFIG_FILE="$HOME/system/configs/bash/imlogin/ip-cred.json";
    # DEFAULT_USER="suggest"

    if [ "$1" = "--config" ]
    then
        jq -r . $CONFIG_FILE;
            
        return;
    fi

    IFS='@';
    read -ra CRED <<< "$1";
    IFS=' ';

     

    if [ ${#CRED[@]} = 2 ]
    then
        USER_NAME=${CRED[0]};
        SERVER_NAME=${CRED[1]};
    else
        # USER_NAME=$DEFAULT_USER;
        SERVER_NAME=${CRED[0]};
        USER_NAME=`jq -r --arg server "$SERVER_NAME" '.[$server].default_user' $CONFIG_FILE`;

    fi    

    IP=`jq -r --arg server "$SERVER_NAME" '.[$server].ip' $CONFIG_FILE`;
    PASSWORD=`jq -r --arg server "$SERVER_NAME" --arg username "$USER_NAME" '.[$server].cred[$username]' $CONFIG_FILE`;

    echo -e "\nLogging to $IP with credentials $USER_NAME:$PASSWORD ...\n";

    echo -e "sshpass -p $PASSWORD ssh $USER_NAME@$IP\n\n";

    sshpass -p $PASSWORD ssh $USER_NAME@$IP;

}
