# ArgonOne

This Arch Linux Package installs all needed scripts and services and configures a Raspberry Pi 3B/3B+ for [Argon ONE Mini Computer Case](https://www.argon40.com/argon1.html).

These are the steps that the installation takes

## Packages needed

Install:

```bash
pacman -S --needed i2c-tools lm_sensors
```

## System Configuration

Edit ```/boot/config.txt``` and add (if needed):

```bash
dtparam=i2c_arm=on
dtparam=i2c-1=on
```

Edit ```/etc/modules-load.d/raspberrypi.conf```and add (if needed):

```bash
i2c-dev
i2c-bcm2835
```

You must reboot for these changes to take effect.

## Virtual Environment Configuration

Create a new Python virtual environment (version 3.3 or higher):

```bash
python -m venv --clear /opt/argonone
source /opt/argonone/bin/activate
pip install pysmbus RPi.GPIO
deactivate
```

## Files

### Config Script

Create and then add permissions:

```bash
chmod 755 /usr/bin/argonone-config
```

## Shutdown Script

Create and then add permissions:

```bash
chmod 755 /lib/systemd/system-shutdown/argononed-poweroff.py
```

### Daemon Config File

Create and then add permissions:

```bash
chmod 666 /etc/argononed.conf
```

## Power Button Script

Create and then add permissions:

```bash
chmod 755 /opt/argonone/bin/argononed.py
```

## Daemon Fan Service

Create and then add permissions:

```bash
chmod 644 /lib/systemd/system/argononed.service
```

Enable to launch automatically:

```bash
systemctl daemon-reload
systemctl enable argononed.service
```
