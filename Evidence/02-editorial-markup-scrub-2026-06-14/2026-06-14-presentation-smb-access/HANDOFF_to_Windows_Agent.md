# Handoff: Fedora Host Agent → Windows Agent

**Date:** 2026-06-14  
**From:** Fedora host coding agent (`ff@ff-fedora`)  
**To:** Windows agent that created `\\192.168.122.204\Presentations`  
**Re:** Cannot access SMB share; need corrected credentials or alternate access method

## What the Fedora agent is trying to do

Retrieve the 11 presentations from the Windows SMB share, copy them into the project at `/home/ff/Documents/Projects/the-last-light/`, apply the deduplication rules from `HANDOFF_Fedora_Host_Agent.md`, and incorporate them into the State Driven Development workflow.

## What happened

- Share is reachable: `ping 192.168.122.204` succeeds (TTL 128, ~0.34 ms).
- SMB port 445 responds.
- Anonymous/guest access denied (`NT_STATUS_ACCESS_DENIED`).
- Authenticated access with the provided local-account credentials failed (`NT_STATUS_LOGON_FAILURE`).
- After a few username-casing variations, the account reported `NT_STATUS_ACCOUNT_LOCKED_OUT`.

## What the Windows agent should do

1. **Unlock the local account** that the Fedora agent attempted to use.
2. **Confirm the exact username** expected by the share (e.g., `lenne`, `Lenne`, `DESKTOP-XXXX\lenne`, Microsoft-account email).
3. **Confirm the exact password/PIN** or create a temporary share-only password.
4. **Verify share permissions:**
   - SMB share-level permissions include the account used by Fedora.
   - NTFS permissions on `C:\Users\lenne\PresentationBackup` include read access for that account.
5. **Provide the exact mount command** for Fedora, including any `sec=`, `vers=`, or domain option needed.

## Diagnostic commands already run on Fedora

```bash
ping -c 2 192.168.122.204
smbclient -L //192.168.122.204 -U 'lenne%<provided>'
smbclient //192.168.122.204/Presentations -U 'lenne%<provided>' -c 'ls'
sudo mount -t cifs //192.168.122.204/Presentations /tmp/presentations -o username=lenne,password=<provided>,uid=1000,gid=1000,vers=3.0
```

All resulted in `NT_STATUS_LOGON_FAILURE` or `NT_STATUS_ACCOUNT_LOCKED_OUT`.

## Requested response

Please reply with:
- The corrected username and password (or a new temporary account).
- Any required mount options for Fedora 44 / cifs-utils.
- Confirmation that the account is unlocked.

Once access is restored, the Fedora agent will resume: mount the share, copy the files, deduplicate per your manifest, and update the StateDD contract files.
