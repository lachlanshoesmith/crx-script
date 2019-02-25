# crx-script by Lachlan Shoesmith (@lachlantula).
# Takes a Chrome Web Store URL and downloads tha appropriate .crx.

from urllib.parse import urlparse
from urllib.request import urlopen

import preferences

extensionURL = input('Extension URL: ')
browserVersion = input('Chromium version (eg. 70.0): ')

parsedURL = urlparse(extensionURL)

urlDomain = parsedURL.netloc
urlPath = parsedURL.path

validDomain = 'chrome.google.com'
validPath = '/webstore/detail'

# In case the user enters '70' or similar...
browserVersion = str(float(browserVersion))

if urlDomain != validDomain or not urlPath.startswith(validPath):
    # if the URL is not a Chrome extension
    print('That\'s not a valid Chrome extension URL.')
    if preferences.verbose:
        print('urlDomain: ' + urlDomain)
        print('urlPath: ' + urlPath)
else:
    urlComponents = urlPath.split('/')
    extensionName = urlComponents[3]
    
    print('Downloading {0}...'.format(extensionName))

    extensionID = urlComponents[4]
    downloadURL = 'https://clients2.google.com/service/update2/crx?response=redirect&acceptformat=crx2,crx3&prodversion={0}&x=id%3D{1}%26installsource%3Dondemand%26uc'.format(browserVersion, extensionID)

    extension = urlopen(downloadURL)

    print('Saving {0} (might take a sec)...'.format(extensionName))

    with open(extensionName + '.crx', 'wb') as f:
        extensionToWrite = extension.read()
        f.write(extensionToWrite)

    print('All done!')
