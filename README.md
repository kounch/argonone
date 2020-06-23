# ArgonOne for Raspberry Pi 4

This Arch Linux Package installs all needed scripts and services and configures a Raspberry Pi 4 for [Argon ONE Mini Computer Case](https://www.argon40.com/argon1.html).

## Installation:
You can either install this package via AUR or GitHub repository in these 2 ways:
### 1. AUR
You can now build and install this package (named in AUR `argonone-git`) via Arch User Repository.
For example, a command to instal using `yay`:
```bash
yay -S argonone-git
```
Please note: AUR is maintained by **[tonnyfettes](https://aur.archlinux.org/account/tonyfettes)** and any issues with AUR shouldn't be posted here (unless they exist in GitHub version of this package). `PKGBUILD` and `argonone.install` might varry in both repositories.

### 2. Manual:
 1. Clone the repository or just download [PKGBUILD](https://raw.githubusercontent.com/Elrondo46/argonone/master/PKGBUILD) and [argonone.install](https://raw.githubusercontent.com/Elrondo46/argonone/master/argonone.install) files.
 2. ```makepkg --install```

## In both situations you might want to enable service with command:

```bash
systemctl enable argononed.service
```

## Thanks to Elrondo, thegeek1977 and the community for helping to patch this branch.
