# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
$HOME = "/home/ubuntu"
$script = <<-SCRIPT
echo I am provisioning the system...
apt-get -y update
apt-get -y install whois python3-pip git lxc tree
python3 -m pip install --upgrade pip
python3 -m pip install ansible
echo I am done provisioning the system...
echo I am rebooting the system
reboot
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "IPv6TrainingLXE2"
  config.ssh.insert_key = true
  config.ssh.forward_agent = true
#  config.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
  config.vm.provision "file", source: "./base", destination: "$HOME/base"
  config.vm.provision "shell", inline: $script 
  config.vm.network "private_network",
                     nic_type: "virtio", 
                     type: "dhcp"

  config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = "1"
  end
end
