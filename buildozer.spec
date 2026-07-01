[app]
title = Prajapati Browser
package.name = prajapatibrowser
package.domain = com.brijesh

source.dir = .
source.include_exts = py,png,jpg,json
version = 1.0

# Kivy ko poori tarah hata diya taaki compilation crash na ho
requirements = python3,android

# Pure Native Android Webview Engine configuration
p4a.bootstrap = webview

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33

[buildozer]
log_level = 2
warn_on_root = 1
