[app]
title = Prajapati Browser
package.name = prajapatibrowser
package.domain = com.brijesh

# Yahan bootstrap ko webview set karna sabse zaroori hai
requirements = python3,android
android.bootstrap = webview

# Permissions aur architectures
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a

# Entry point file ka naam main.py hona chahiye
source.include_exts = py,png,jpg,kv,atlas
