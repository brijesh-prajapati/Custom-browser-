import os
import time
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Core Android Native Interface Hooks
PythonActivity = autoclass('org.kivy.android.PythonActivity')
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')

class PrajapatiBrowser:
    def __init__(self):
        self.launch_webview()

    @run_on_ui_thread
    def launch_webview(self):
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        
        # Enable JavaScript and Storage for smooth AI Chat UI
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setDatabaseEnabled(True)
        settings.setAllowFileAccess(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # Target Live Website URL
        target_url = "https://brijesh-prajapati.github.io/Custom-browser-/"
        webview.loadUrl(target_url)
        
        # Set webview as the full screen view
        activity.setContentView(webview)

if __name__ == '__main__':
    # Engine start
    PrajapatiBrowser()
    
    # Keep the background python process alive safely
    while True:
        time.sleep(1)
        
