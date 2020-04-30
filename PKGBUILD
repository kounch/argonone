# Maintainer: Elrondo46 (https://github.com/Elrondo46)
# Contributor: kounch (https://github.com/kounch)

pkgname=argonone-rpi4
pkgver=20191209
pkgrel=1
pkgdesc="Argon One Service and Control Scripts"
arch=('any')
url='https://download.argon40.com/argon1.sh'
license=('GPL3')
depends=('i2c-tools' 'libffi' 'lm_sensors' 'python>=3.3')
provides=('argonone')
install=argonone.install

source=(
  "https://raw.githubusercontent.com/Elrondo46/argonone/master/argonone-config"
  "https://raw.githubusercontent.com/Elrondo46/argonone/master/argononed-poweroff.py"
  "https://raw.githubusercontent.com/Elrondo46/argonone/master/argononed.conf"
  "https://raw.githubusercontent.com/Elrondo46/argonone/master/argononed.py"
  "https://raw.githubusercontent.com/Elrondo46/argonone/master/argononed.service"
  )

sha256sums=(
  "41831f2796691322131061a23a2c61b01d9d124416854963a2ba9c47a72d0850"
  "25cfb38db6c8804dd7091fc1af3ee3505a95394b799e998e81a6d59f721cae09"
  "f6f82283a286c9694a5adc6db842fca2e75845f1ccf0bacfb7ce2efa3c8eaec3"
  "6a82dd456f02ec5f2de4dc9974eed847670247c9dbf120124acfa6c0b6e5713f"
  "1db1bc647690db29339ef4317b10738fe7fdbc379aad2149c9d0d353c42a3db4"
)

package() {
  install -Dm755 "${srcdir}"/argonone-config "${pkgdir}"/usr/bin/argonone-config
  install -Dm755 "${srcdir}"/argononed-poweroff.py "${pkgdir}"/usr/lib/systemd/system-shutdown/argononed-poweroff.py
  install -Dm666 "${srcdir}"/argononed.conf "${pkgdir}"/etc/argononed.conf
  install -Dm755 "${srcdir}"/argononed.py "${pkgdir}"/opt/argonone/bin/argononed.py
  install -Dm644 "${srcdir}"/argononed.service "${pkgdir}"/usr/lib/systemd/system/argononed.service
}
