# utils
Utility repo to store scripts and the like.

## router.py
Script that interacts with a Livebox router through its web UI, using Selenium and Chrome. Currently it can:

- enable and disable wifi
- reset the connection

Dependencies:

- [Chrome/Chromium web browser](https://www.chromium.org/Home)
- [Python bindings for Selenium](https://pypi.python.org/pypi/selenium)
- [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/)
- Environment variables: `ROUTER_UI_URL`, `ROUTER_UI_PASSWD`

Tested on Linux.
