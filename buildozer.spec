[app]
title = Firewall Master
package.name = firewallmaster
package.domain = org.choyvlog
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# 1. Dagdagan natin ang requirements para mas stable ang Python
requirements = python3==3.11.2,kivy,psutil

orientation = portrait
fullscreen = 0

# 2. Siguraduhin natin ang permissions
android.permissions = KILL_BACKGROUND_PROCESSES, PACKAGE_USAGE_STATS, INTERNET

# 3. Importante: I-set ang API at NDK version nang maayos
android.api = 33
android.minapi = 21

# Iwanang blanko ang mga paths para ang Buildozer ang kumuha ng tama
android.sdk_path = 
android.ndk_path = 
# Gamitin ang NDK version na stable para sa psutil compilation
android.ndk = 25b

# 4. Architecture - Isama ang v7a para sa mas maraming phone support
android.archs = arm64-v8a, armeabi-v7a

# 5. Force the use of master branch for python-for-android fixes
p4a.branch = master

android.accept_sdk_license = True
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1