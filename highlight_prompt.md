a Chrome Manifest V3 extension that when activated highlight the <h1> on the page to be with red background

## debugging notes

make sure the popup.js is loaded after the Activate Extension button is defined in the popup.html

make sure when the user clicks the Activate Extension button, the highlight action is triggered on the current active tab

Update your `manifest.json` file to include the "scripting" permission:

```json
{
  ...
  "permissions": [
    "activeTab",
    "scripting"
  ],
  ...
}
```

inside  `popup.js` update to use the `chrome.scripting.executeScript` API:

```javascript
function activateExtension() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    // Replace this line
    // chrome.scripting.executeScript({
    //   target: { tabId: tabs[0].id },
    //   files: ["content_script.js"],
    // });

    // With this line
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      files: ["content_script.js"],
    }, () => {
      // Add this line to send a message to the content script
      chrome.tabs.sendMessage(tabs[0].id, { action: "highlightH1" });
    });
  });
}