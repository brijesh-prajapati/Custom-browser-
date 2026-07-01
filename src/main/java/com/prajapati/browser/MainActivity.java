package com.prajapati.browser;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView myWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Direct Native Fullscreen WebView Instantiation
        myWebView = new WebView(this);
        WebSettings webSettings = myWebView.getSettings();
        
        // Runtime Sandbox Web Configurations
        webSettings.setJavaScriptEnabled(True);
        webSettings.setDomStorageEnabled(True);
        webSettings.setDatabaseEnabled(True);
        webSettings.setBuiltInZoomControls(False);
        
        myWebView.setWebViewClient(new WebViewClient());
        
        // Target Application Route Setup
        myWebView.loadUrl("https://brijesh-prajapati.github.io/Custom-browser-/");

        setContentView(myWebView);
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

