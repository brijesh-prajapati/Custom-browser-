import os
import sys
import time

def main():
    print("Prajapati Browser Engine Initializing...")
    
    # Android window system initialization ke liye short delay taaki mActivity None na mile
    time.sleep(3) 
    
    try:
        from jnius import autoclass
        from android.runnable import run_on_ui_thread

        # Android Native Component Load
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        
        # Safe check logic jab tak activity mil nahi jaati
        activity = None
        for i in range(10):
            activity = PythonActivity.mActivity
            if activity is not None:
                break
            print("Waiting for Android Native Activity Window...")
            time.sleep(1)

        if activity is None:
            print("Core Critical Error: Android Activity interface missing.")
            return

        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')

        @run_on_ui_thread
        def launch():
            try:
                wv = WebView(activity)
                settings = wv.getSettings()
                
                # Full Browser Capabilities Enable
                settings.setJavaScriptEnabled(True)
                settings.setDomStorageEnabled(True)
                settings.setDatabaseEnabled(True)
                settings.setAllowFileAccess(True)
                
                wv.setWebViewClient(WebViewClient())
                wv.loadUrl("https://brijesh-prajapati.github.io/Custom-browser-/")
                activity.setContentView(wv)
                print("Webview loaded successfully inside Native Main Window.")
            except Exception as e:
                print(f"UI Thread Crash Fallback: {str(e)}")

        launch()
    except Exception as e:
        print(f"Native initialization bypass active: {str(e)}")

    # Python application main loop to keep process alive
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
    
