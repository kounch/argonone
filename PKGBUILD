# Maintainer: kounch (https://github.com/kounch)

pkgname=argonone
pkgver=20190217
pkgrel=1
pkgdesc="Argon One Service and Control Scripts"
arch=('any')
url='https://download.argon40.com/argon1.sh'
license=('GPL3')
depends=('i2c-tools' 'lm_sensors' 'python>=3.3')
provides=('argonone')
install=argonone.install

source=(
  "https://raw.githubusercontent.com/kounch/argonone/master/argonone-config"
  "https://raw.githubusercontent.com/kounch/argonone/master/argononed-poweroff.py"
  "https://raw.githubusercontent.com/kounch/argonone/master/argononed.conf"
  "https://raw.githubusercontent.com/kounch/argonone/master/argononed.py"
  "https://raw.githubusercontent.com/kounch/argonone/master/argononed.service"
  )

sha256sums=(
  "41831f2796691322131061a23a2c61b01d9d124416854963a2ba9c47a72d0850"
  "e5f8fa9cfeee93790654f90a70b3cb7df9fa1a760fb4f3b042c731cd9cc40f74"
  "f6f82283a286c9694a5adc6db842fca2e75845f1ccf0bacfb7ce2efa3c8eaec3"
  "dfa5dc21b5b474efe6f2b2acc105e7052aad1bfab6066a7318e17f5016468815"
  "1db1bc647690db29339ef4317b10738fe7fdbc379aad2149c9d0d353c42a3db4"
)

package() {
  install -Dm755 "${srcdir}"/argonone-config "${pkgdir}"/usr/bin/argonone-config
  install -Dm755 "${srcdir}"/argononed-poweroff.py "${pkgdir}"/usr/lib/systemd/system-shutdown/argononed-poweroff.py
  install -Dm666 "${srcdir}"/argononed.conf "${pkgdir}"/etc/argononed.conf
  install -Dm755 "${srcdir}"/argononed.py "${pkgdir}"/opt/argonone/bin/argononed.py
  install -Dm644 "${srcdir}"/argononed.service "${pkgdir}"/usr/lib/systemd/system/argononed.service
}
