# Bentley's Stardew Mod Manager

A custom Android companion for Stardew Valley on Android.

## Included in the first build
- Android Storage Access Framework folder grants with persisted permissions
- Shared StardewValley and Mods folder selection
- ZIP extraction into the selected Mods directory, with path traversal checks
- Installed mod folder and manifest inventory
- SMAPI log import with error/warning summaries
- Save XML inspection and core character-stat editing
- Automatic pre-edit save backups
- Manual backups and backup restore
- Dark custom interface and original vector app icon

## Save editor fields
Character name, gold, health, maximum health, stamina, and maximum stamina.

The app validates numeric fields and creates a copy of the original save under StardewValley/BentleyBackups before writing edited XML.

## Storage notes
Android's system picker (DocumentsUI) is used. Android may refuse access to Android/data even when a tree picker is used. The app does not claim that All files access bypasses scoped-storage restrictions. Choose the shared StardewValley folder and Mods folder when available.

## Build
Requires JDK 17 and Gradle 8.9. Run gradle assembleDebug.

## Package
com.bentleyplayz.stardewmodmanager

## Developer
Bentley Playz
