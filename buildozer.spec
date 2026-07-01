[app]
title = Prajapati Browser
package.name = prajapatibrowser
package.domain = com.brijesh

# Source targets
source.dir = .
source.include_exts = py,png,jpg,json

# Version configuration matrix
version = 1.0

# Base engine requirements
requirements = python3,android,kivy

# Standard stable bootstrap layout
p4a.bootstrap = sdl2

# Android settings targets
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 1
