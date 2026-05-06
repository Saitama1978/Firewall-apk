[app]

# (str) Title of your application
title = Mobile Firewall Pro

# (str) Package name
package.name = firewallpro

# (str) Package domain (important)
package.domain = org.renantefullo

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Application version
version = 1.0

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# ==============================
# ANDROID CONFIG (IMPORTANT)
# ==============================

[buildozer]

# (int) Log level (0 = error only, 2 = full debug)
log_level = 2

# (int) Warn on deprecated
warn_on_root = 1


[app:android]

# ✅ STABLE SETTINGS (fix sa error mo)
android.api = 31
android.minapi = 21
android.ndk = 25b

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Permissions (optional dagdagan kung need mo)
android.permissions = INTERNET

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Use SDL2 (default)
android.bootstrap = sdl2

# (optional) Icon
#icon.filename = %(source.dir)s/icon.png

# (optional) Splash
#presplash.filename = %(source.dir)s/presplash.png


# ==============================
# PYTHON-FOR-ANDROID FIX
# ==============================

# 🔥 IMPORTANT (fix sa gradlew failure)
p4a.branch = stable


# ==============================
# BUILD OPTIONS
# ==============================

# Copy libs instead of symlink
copy_libs = 1

# Use local recipes if needed
#p4a.local_recipes = ./recipes


# ==============================
# DEBUGGING
# ==============================

# Enable verbose logs
log_level = 2