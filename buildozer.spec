[app]

# (Pangalan ng App)
title = Firewall Master
# (Shortcut name - walang spaces)
package.name = firewallmaster
# (Domain mo - pwedeng kahit ano)
package.domain = org.choyvlog

# (Source code location)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (App Version)
version = 1.0

# (MAHALAGA: Isinama ang psutil dito)
requirements = python3,kivy,psutil

# (Custom settings para sa hitsura)
orientation = portrait
fullscreen = 0

# (Permissions para sa Firewall functionality)
# Tandaan: Ang KILL_BACKGROUND_PROCESSES ay kailangan para sa STOP button
android.permissions = KILL_BACKGROUND_PROCESSES, PACKAGE_USAGE_STATS, INTERNET

# (Target Android version - API 33 ang standard ngayon)
android.api = 33
android.minapi = 21
android.ndk_path = 
android.sdk_path = 

# (Architecture para sa modernong phones)
android.archs = arm64-v8a

# (Iba pang technical settings)
android.accept_sdk_license = True
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1