[app]
title = Prajapati Browser
package.name = prajapatibrowser
package.domain = com.brijesh

# Source code files mapping
source.dir = .
source.include_exts = py,png,jpg,json

# Is requirement se build crash nahi hoga
requirements = python3,android

# Pure Native Webview Bootstrap configuration
android.bootstrap = webview
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33

# Build system log behavior
p4a.branch = master
