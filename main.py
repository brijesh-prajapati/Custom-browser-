import os
import sys
import time

def main():
    print("Initializing Prajapati AI Browser Sandbox Engine...")
    
    try:
        from jnius import autoclass
        # Safe Android background runtime initialization
        PythonService = autoclass('org.kivy.android.PythonService')
        activity = PythonService.mService
        
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        
        # UI Native Loop Thread Executor
        from android.runnable import run_on_ui_thread
        
        @run_on_ui_thread
        def setup_webview():
            wv = WebView(activity)
            settings = wv.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            
            wv.setWebViewClient(WebViewClient())
            wv.loadUrl("https://brijesh-prajapati.github.io/Custom-browser-/")
            activity.setContentView(wv)
            
        setup_webview()
    except Exception as e:
        print(f"Fallback check active. Error logs: {str(e)}")

    # Core keep alive process loop
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
    
