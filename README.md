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

Currently it only supports [Feather](https://github.com/khcrysalis/Feather).

[AltStore](https://altstore.io/) and [SideStore](https://sidestore.io/) sources are available - but installation is **not supported.**  
This is because the app is not signed during the build/release process.  
The open PR [add ipa signing; integrate repo; add entitlements #418](https://github.com/kodjodevf/mangayomi/pull/418) hopes to address this in the future.

## Features

- [x] Displays new releases within 24hrs
- [x] Files are direct links to the GitHub repo
- [x] News banners and captions vary between minor and patch versions
- [x] Provides version and formatted date in the news title for readability
- [x] Automatically purges old releases if they are removed from the main repo
- [ ] Missing something? Let me know!

## Credit

Thank you to [Balackburn](https://github.com/Balackburn) for their Apollo AltStore source implementation which was used to inform this one.
