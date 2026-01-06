#!/bin/bash
#

# Check if script is being executed as the superuser priviliges
if [[ $UID -ne 0 ]]
then
	echo "Please run with the sudo or root."
	exit 1
fi

# if the user doesn't provide atleast one arg .. hint them
if [[ "${#}" -lt 1 ]]
then
	echo "Please provide atleast one argument."
	echo "Example usage: "
	echo "$0 USERNAME [COMMENT]"
	exit 1
fi

# the first param is the username
USERNAME=$1 # OR "${1}"

# the rest of the params are the comments
shift
COMMENT=$@

# generate the password 
PASSWORD=$(echo $(( $( date +%s%N ) * ($RANDOM + 1) ** 10 )) | tr -d "-")

# create the user with the password
sudo useradd -c "$COMMENT" -m $USERNAME

# Check if the useradd command succeeded or not
if [[ $? -ne 0 ]]
then 
	echo "The account could not be created!"
	exit 1
fi

# set the password
# echo $PASSWORD | sudo passwd --stdin $USERNAME
echo "$USERNAME:$PASSWORD" | sudo chpasswd


# check to see if the passwd command succeeded
if [[ $? -ne 0 ]]
then
        echo "Password could not be set!"
        exit 1
fi

# Force password change on first login
passwd -e USERNAME i # -e means expire old one

# display the username, password, and the host where the user is created

echo
echo "Username: $USERNAME"
echo
echo "PASSWORD: $PASSWORD"
echo
echo "$(hostname)"
