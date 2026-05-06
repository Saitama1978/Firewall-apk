[app]
title = RAMSaver Pro
package.name = ramsaverpro
package.domain = org.renante
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Gumamit muna tayo ng basic requirements para siguradong mag-build
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# Stable versions para sa GitHub Actions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1