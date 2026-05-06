[app]

# (str) Title of your application
title = Mobile Firewall Pro

# (str) Package name
package.name = firewallpro

# (str) Package domain (needed for android packaging)
package.domain = org.renantefullo

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# MAHALAGA: Kasama dito ang psutil para sa monitoring ng apps
requirements = python3,kivy,psutil

# (list) Permissions
# MAHALAGA: Kailangan ito para makita at ma-stop ang ibang apps
android.permissions = INTERNET, KILL_BACKGROUND_PROCESSES

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is to use start.py
orientation = portrait

# (list) List of service to declare
# Pwede mong lagyan ito sa future kung gusto mong tumakbo ang firewall sa background
services = 

# (str) Developer Credit
# Nilalagay natin ito sa metadata ng app
author = Renante Fullo

# (str) Support email
author_email = reyfull22@gmail.com

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
