from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from jnius import autoclass

class BrowserApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Native Android Android Components
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        
        activity = PythonActivity.mActivity
        webview = WebView(activity)
        
        # Disable CORS & Enable Javascript
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccessFromFileURLs(True)
        settings.setAllowUniversalAccessFromFileURLs(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # Aapka direct interface link
        webview.loadUrl("https://brijesh-prajapati.github.io/Personal-ai/")
        
        layout.add_widget(webview)
        return layout

if __name__ == '__main__':
    BrowserApp().run()
  
