# Android Storage Architecture

The app will use Android's Storage Access Framework.

Primary shared directory:
StardewValley/

Mods directory:
StardewValley/Mods/

SMAPI launcher data:
Android/data/abc.smapi.gameloader/

The app must test actual read/write access after a folder
grant. It must not assume that Android/data is accessible.

Persistent URI permissions should be retained where supported.

If access to a directory is denied, the app must explain
the limitation and provide an alternative workflow.
