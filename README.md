# vagrantlxc
Vagrant Non-Privileged Ubuntu 16.04 LXC Environment 

# Instructions
1. Install Virtualbox and Vagrant on target machine
2. Run "vagrant up" in this directory
3. Enter newly created box by "vagrant ssh" from within this directory
4. From "base" directory run "ansible-playbook -e @./instances/singleUbuntuUser.yml site.yml"
5. Log into environment using assigned username/password through the base vagrant box
6. Obtain list of defined lxc hosts by running "lxc-ls -f"
7. Use lxc-attach -n LXCHOSTNAME to connect to each container in exercise

Instance definition files are user defined and can be edited.  Depending on environment end-user can use the provided templates to customize as necessary.

Field Definitions
containnarch: The hardware environment lxc is running on (as supported by lxc)
## global variables
* shell: default shell for defined users
* bridges: The number of bridges a non-privileged user may define
## users
The list of users to create a non-privileged  environnment for.  Each account allows for simple username based authentication.
### assigned_bridges
A list of bridges to assign to a particular user (lxcbr0 is common to all by default).  These bridges are intented to be unique per user.
