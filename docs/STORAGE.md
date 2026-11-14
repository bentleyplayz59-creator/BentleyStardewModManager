# Android Storage Architecture

The app targets the user's actual SMAPI installation:

`/storage/emulated/0/Android/data/abc.smapi.gameloader/files/`

The user grants this exact `files` directory through Android DocumentsUI using `ACTION_OPEN_DOCUMENT_TREE`. The app requests read, write, and persistable URI permissions and stores the granted tree URI.

A successful tree grant covers descendants such as:

- `Mods/`
- `Saves/`
- `ErrorLogs/`
- `Stardew Assets/Content/`
- `save-backups/`

After selection, the app checks that the selected directory is named `files`, lists its children, creates a temporary permission-test file, writes to it, and removes it. It reports a failure if the picker does not grant read/write access.

Android versions may prevent DocumentsUI from selecting `Android/data` or its descendants. The app must not claim access unless the user completes the grant and the read/write test succeeds. It must not use ADB or claim that broad storage permission bypasses Android's restrictions.

Save files can also be opened individually through the system document picker. Backups created by the app are stored in the granted SMAPI `files/` directory under `BentleyBackups/`.
