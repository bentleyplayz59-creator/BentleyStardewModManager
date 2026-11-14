# Bentley's Stardew Mod Manager

A custom Android companion for Stardew Valley on Android.

## Included
- Android DocumentsUI folder grant with persisted read/write permissions
- Targeted access to the SMAPI installation's actual `files/` directory
- Read/write permission test after folder selection
- ZIP extraction into the SMAPI `files/Mods/` directory, with path traversal checks
- Installed mod folder and manifest inventory
- SMAPI log import with error/warning summaries
- Save XML inspection and core character-stat editing
- Automatic pre-edit save backups
- Manual backups and backup restore
- Dark custom interface and original vector app icon

## Storage location
The app asks the user to select:

`/storage/emulated/0/Android/data/abc.smapi.gameloader/files/`

One successful tree grant covers its child folders, including `Mods`, `Saves`, `ErrorLogs`, `Stardew Assets`, and `save-backups`. The app verifies actual read/write access before treating the grant as usable.

**Android limitation:** Some Android versions block selecting `Android/data` and descendants in DocumentsUI. The app does not bypass this restriction, use ADB, or pretend that a failed grant succeeded. The user must test the picker on their device.

## Save editor fields
Character name, gold, health, maximum health, stamina, and maximum stamina. The app creates a copy of the original save under `files/BentleyBackups/` before writing edited XML.

## Build
Requires JDK 17 and Gradle 8.9. Run `gradle assembleDebug`.

## Package
`com.bentleyplayz.stardewmodmanager`

## Developer
Bentley Playz
