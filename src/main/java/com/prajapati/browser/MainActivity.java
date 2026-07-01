package com.prajapati.browser;

import android.app.Activity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.EditText;
import android.view.inputmethod.EditorInfo;
import android.widget.TextView;

public class MainActivity extends Activity {
    private WebView myWebView;
    private EditText urlInput;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        LinearLayout mainLayout = new LinearLayout(this);
        mainLayout.setOrientation(LinearLayout.VERTICAL);

        // Upar ek input box jisme URL likh sako
        urlInput = new EditText(this);
        urlInput.setSingleLine(true);
        urlInput.setImeOptions(EditorInfo.IME_ACTION_GO);
        urlInput.setHint("Enter URL here...");
        urlInput.setText("https://bing.com");
        mainLayout.addView(urlInput);

        myWebView = new WebView(this);
        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setDatabaseEnabled(true);
        
        myWebView.setWebViewClient(new WebViewClient());
        myWebView.loadUrl("https://bing.com");

        LinearLayout.LayoutParams webViewParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.MATCH_PARENT);
        mainLayout.addView(myWebView, webViewParams);

        setContentView(mainLayout);

        urlInput.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_ACTION_GO || (event != null && event.getKeyCode() == KeyEvent.KEYCODE_ENTER)) {
                    String url = urlInput.getText().toString().trim();
                    if (!url.startsWith("http://") && !url.startsWith("https://")) {
                        url = "https://" + url;
                    }
                    myWebView.loadUrl(url);
                    return true;
                }
                return false;
            }
        });
    }

    @Override
    public void onBackPressed() {
        if (myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
