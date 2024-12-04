#!/bin/bash
echo "uninstall conflicting packages for Docker"
echo
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# setup dockers apt repo

echo "Adding Dockers official GPG key"

sudo apt-get update
echo
sudo apt-get install ca-certificates curl -y
echo
sudo install -m 0755 -d /etc/apt/keyrings
echo
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo

echo "Adding the repository to Apt sources:"
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
echo 
sudo apt-get install -y \
docker-ce \
docker-ce-cli \
containerd.io \
docker-buildx-plugin \
docker-compose-plugin
echo 

echo "Chekcing to see if docker installed correctly"
echo
sudo docker run hello-world

echo 
echo "Downloading and installing DOCKER DESKTOP"

sudo apt-get update

sudo wget "https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64&_gl=1*boqfpu*_ga*MTA4OTcwODE3NS4xNzI3MTAxOTky*_ga_XJWPQMJYHQ*MTcyNzEwMTk5Mi4xLjEuMTcyNzEwNTA5NC40NS4wLjA." -O docker-desktop-amd64.deb

sudo apt-get install ./docker-desktop-amd64.deb