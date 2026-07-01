import os
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Android System Classes Hooks
Activity = autoclass('org.kivy.android.PythonActivity').mActivity
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')

class PrajapatiBrowser:
    def __init__(self):
        self.create_window()

    @run_on_ui_thread
    def create_window(self):
        activity = Activity
        webview = WebView(activity)
        
        # Webview runtime setups
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowUniversalAccessFromFileURLs(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # Aapki live application url load target
        target_url = "https://brijesh-prajapati.github.io/Personal-ai/"
        webview.loadUrl(target_url)
        
        activity.setContentView(webview)

if __name__ == '__main__':
    # Initialize Core Application Engine
    PrajapatiBrowser()
    
    # Keeping main python loop alive safely
    import time
    while True:
        time.sleep(1)
        
