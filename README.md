# ArgonOne for Raspberry Pi 4

This Arch Linux Package installs all needed scripts and services and configures a Raspberry Pi 4 for [Argon ONE Mini Computer Case](https://www.argon40.com/argon1.html).

## How to use

 1. Clone the repository or just download [PKGBUILD](https://raw.githubusercontent.com/Elrondo46/argonone/master/PKGBUILD) and [argonone.install](https://raw.githubusercontent.com/Elrondo46/argonone/master/argonone.install) files
 2. ```makepkg --install```

Enable it before reboot:

```bash
systemctl enable argononed.service
```

## This repo will be destroy if kounch patch his repo for Raspberry Pi 4, don't want to fork, just helping users wants to have a ready to use solution

## Thanks to thegeek1977 to help patching this
