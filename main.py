import os
import sys
import time

def main():
    print("Starting Prajapati Browser Engine...")
    try:
        from jnius import autoclass
        from android.runnable import run_on_ui_thread

        # Native Hooks for Android Webview Bootstrap
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')

        @run_on_ui_thread
        def launch():
            wv = WebView(activity)
            settings = wv.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            settings.setAppCacheEnabled(True)
            
            wv.setWebViewClient(WebViewClient())
            wv.loadUrl("https://brijesh-prajapati.github.io/Custom-browser-/")
            activity.setContentView(wv)

        launch()
    except Exception as e:
        print(f"Native initialization engine bypass active: {str(e)}")

    # Keeping main execution thread active
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
    
