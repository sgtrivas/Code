
#!/bin/bash
# sed -i -e 's/\r$//' ADMinstall.sh
#install Java runtime environment
###sudo apt install default-jre

#install Java SDK 
###sudo apt install default-jdk

#install adb and fastboot: 
###sudo apt install adb fastboot

#for Debian/Ubuntu scrcpy install
#info located at https://github.com/Genymobile/scrcpy
###sudo apt install ffmpeg libsdl2-2.0-0 adb wget \
###                 gcc git pkg-config meson ninja-build libsdl2-dev \
###                 libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
###                 libswresample-dev libusb-1.0-0 libusb-1.0-0-dev

#clone the repo to execute install script

###git clone https://github.com/Genymobile/scrcpy

##cd scrcpy
###./install_release.sh




# Array of packages to check and install
packages=(
  openjdk-17-jre
  openjdk-17-jdk
  adb
  fastboot
  ffmpeg
  libsdl2-2.0-0
  wget
  gcc
  git
  pkg-config
  meson
  ninja-build
  libsdl2-dev
  libavcodec-dev
  libavdevice-dev
  libavformat-dev
  libavutil-dev
  libswresample-dev
  libusb-1.0-0
  libusb-1.0-0-dev
)

# Function to check if a package is installed and install it if not
install_package() {
  package=$1
  if dpkg -s $package >/dev/null 2>&1; then
    echo "$package is already installed."
  else
    echo "$package is not installed. Installing..."
    sudo apt-get install -y $package
    if [ $? -eq 0 ]; then
      echo "$package installed successfully."
    else
      echo "Error installing $package."
      exit 1
    fi
  fi
}

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install required packages
for package in "${packages[@]}"; do
  install_package $package
done

# Clone the scrcpy repository
if [ ! -d "scrcpy" ]; then
  echo "Cloning scrcpy repository..."
  git clone https://github.com/Genymobile/scrcpy.git
  if [ $? -eq 0 ]; then
    echo "Repository cloned successfully."
  else
    echo "Error cloning repository."
    exit 1
  fi
else
  echo "scrcpy repository already exists."
fi

# Change to the scrcpy directory
cd scrcpy || exit

# Run the install_release.sh script
echo "Running install_release.sh..."
chmod +x install_release.sh
./install_release.sh

if [ $? -eq 0 ]; then
  echo "scrcpy installation completed successfully."
else
  echo "Error running install_release.sh."
  exit 1
fi

echo "Downloading ADM..."
wget https://github.com/jpage4500/AndroidDeviceManager/releases/download/24.08.01/AndroidDeviceManager.jar

echo "All tasks completed. TO EXECUTE ADM RUN java -jar AndroidDeviceManager.jar"
