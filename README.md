<p align="center"><img src="images/headers/readme_header_black.webp" alt="Mangayomi Banner"/></p>

<a href="https://intradeus.github.io/http-protocol-redirector?r=altstore://source?url=https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/altstore_button.png" width="200"></a>
&nbsp;
<a href="https://intradeus.github.io/http-protocol-redirector?r=feather://source/https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/feather_button.png" width="200"></a>
&nbsp;
<a href="https://intradeus.github.io/http-protocol-redirector?r=sidestore://source?url=https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/sidestore_button.png" width="200"></a>
&nbsp;
<a href="https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/url_button.png" width="200"></a>

-----

# Sideloading Source

An unofficial repository source for [Mangayomi](https://github.com/kodjodevf/mangayomi).

It will automatically stay up-to-date via. a GitHub workflow action that polls the main repo each day.  
This repo does not rehost releases. Instead it fetches the direct `.ipa` link and inserts new entries into [apps.json](apps.json)

Currently it supports [Feather](https://github.com/khcrysalis/Feather) and [SideStore](https://sidestore.io/).  
It may work with [AltStore](https://altstore.io/) - but it has not been tested as I am yet to determine the exact entitlements and privacy provisions specified in the [compatibility documentation](https://faq.altstore.io/developers/make-a-source#app-permissions).

## Credit

Thank you to [Balackburn](https://github.com/Balackburn) for their Apollo AltStore source implementation which was used to inform this one.
