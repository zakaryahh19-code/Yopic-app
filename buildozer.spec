[app]
title = Yopic
package.name = Yopic
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ico
source.include_patterns = assets/*
version = 0.1
requirements = hostpython3==3.11.9,python3==3.11.9,kivy==2.3.0,kivymd==1.1.1,pillow
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/assets/icon.png

# Android specific
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.accept_sdk_license = True
android.archs = armeabi-v7a
android.allow_backup = True

# p4a fix for Python 3.11 / 3.13
p4a.branch = master
p4a.bootstrap = sdl2

# iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.allowed = false

[buildozer]
log_level = 1
warn_on_root = 1
