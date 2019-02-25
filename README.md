# crx-script

Downloads the .crx (extension file) for a provided extension and Chrome version.

## Why would I use this?

If you're attempting to de-Googlify yourself you may have come across [ungoogled-chromium](https://github.com/Eloston/ungoogled-chromium), which does not support the downloading of extensions from the Chrome Web Store. This program handles that.

## My .crx files don't work!

Enter the following URL in Chrome/ium: `chrome://flags/#extension-mime-request-handling` and set the appropriate value to `Always prompt for install`. Relaunch your browser and attempt to drag-and-drop your respective .crx file in.

If that doesn't work it is probable that your input is wrong. If not, create an issue or submit a pull request! I'm still new to this.
