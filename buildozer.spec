[app]
title = Prajapati Browser
package.name = prajapatibrowser
package.domain = com.brijesh

# Source directories
source.dir = .
source.include_exts = py,png,jpg,json

# Explicit Version Definition Matrix (Crucial Fix)
version = 1.0

# Requirements setup
requirements = python3,android

# Correct Bootstrap Parameter (Crucial Fix)
p4a.bootstrap = webview

# System Architectures and Permissions
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 1
