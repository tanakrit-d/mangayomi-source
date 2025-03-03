<p align="center">
  <img src="images/header/readme_header.png" alt="Mangayomi Banner"/>
</p>

<a href="altstore://source?url=https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/altstore_button.png" width="200"></a>
&nbsp;
<a href="feather://source?url=https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/feather_button.png" width="200"></a>
&nbsp;
<a href="sidestore://source?url=https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/sidestore_button.png" width="200"></a>
&nbsp;
<a href="https://raw.githubusercontent.com/tanakrit-d/mangayomi-source/refs/heads/main/apps.json"><img src="images/buttons/url_button.png" width="200"></a>

-----

# Sideloading Source

An unofficial repository source for [Mangayomi](https://github.com/kodjodevf/mangayomi).

It will automatically stay up-to-date via. a GitHub workflow action that polls the main repo each day.  
This repo does not rehost releases. Instead it fetches the direct `.ipa` link and inserts new entries into [apps.json](apps.json)

Currently it only supports [Feather](https://github.com/khcrysalis/Feather).  
It may work with AltStore and SideStore - but it has not been tested.  
I am yet to determine the exact entitlements and privacy provisions specified in the [compatibility](https://faq.altstore.io/developers/make-a-source#app-permissions) documentation.

## Credit

Thank you to [Balackburn](https://github.com/Balackburn) for their Apollo AltStore source implementation which was used to inform this one.
