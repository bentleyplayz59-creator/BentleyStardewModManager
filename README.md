# Bentley's Stardew Mod Manager

A custom Android application for managing Stardew Valley mods
on Android devices running SMAPI.

## Planned features

- Import and inspect mod ZIP archives
- Install and update mods
- Remove and back up mods
- Detect duplicate mods
- Read and analyze SMAPI logs
- Identify missing dependencies
- Inspect mod manifests and versions
- Manage Stardew Valley save backups
- Storage Access Framework integration
- Persistent folder permissions where supported
- Android storage permission diagnostics

## Storage locations

SMAPI launcher data:
Android/data/abc.smapi.gameloader/

Shared Stardew Valley data:
StardewValley/

Mods:
StardewValley/Mods/

## Application ID

com.bentleyplayz.stardewmodmanager

## Developer

Bentley Playz

## Important

The application will not modify files outside explicitly
authorized locations. Storage access will be checked at runtime.
