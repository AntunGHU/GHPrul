# 0'48

# Samo za Win i Mac napravila ekipa GH-aba! Skida se sa "https://desktop.github.com" ali zahtjeva GH account i optionaly 2 factor authetification.

# * Za Linux napravila Comunity: https://www.vitainbeta.org/2022/07/29/installing-github-desktop-linux/

# Installing GitHub Desktop on Linux thanks to The Linux Fork     29 July 2022 Lorenzo

# GitHub Desktop is an open-source version of the famous app based on Electron. This version was written in TypeScript and React. For more information, see the GitHub Desktop – The Linux Fork where you can find links to the repository on GitHub, download links (copied below), and so on.

# The installation process is surprisingly easy. Depending on your OS, have a look at the following:
# GitHub Desktop on Debian or Ubuntu: Use the following commands to configure the package repository:

# ? $ wget -qO - https://packagecloud.io/shiftkey/desktop/gpgkey | sudo apt-key add -
# ? $ sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/shiftkey/desktop/any/ any main" > /etc/apt/sources.list.d/packagecloud-shiftky-desktop.list'
# ? $ sudo apt-get update

# Next, installation:

# ? $ sudo apt install github-desktop

# You just made it!
# If you need more information or are just curious to know more, have a look at The Linux Fork repository.
# The purpose of this application is stated on their official website:
# “Focus on what matters instead of fighting with Git. Whether you’re new to Git or a seasoned user, [it] simplifies your development workflow.”
