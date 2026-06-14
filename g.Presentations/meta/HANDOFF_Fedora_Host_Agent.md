# Handoff: Copy and Deduplicate Presentations on Fedora Host

## Source (Windows VM SMB Share)

- **Share name:** `Presentations`
- **UNC path:** `\\192.168.122.204\Presentations`
- **Local path on Windows VM:** `C:\Users\lenne\PresentationBackup`
- **Windows VM user:** `lenne`
- **Network profile:** Private (SMB-In firewall rule enabled)
- **SMB version:** SMB 2/3 enabled, security signature required, unencrypted access rejected

## How to mount from Fedora

```bash
# Install cifs-utils if not already present
sudo dnf install -y cifs-utils

# Create a local mount point
sudo mkdir -p /mnt/presentations

# Mount using the Windows VM user credentials
# You will be prompted for lenne's Windows password
sudo mount -t cifs //192.168.122.204/Presentations /mnt/presentations -o username=lenne,vers=3.0,sec=ntlmssp

# Verify contents
ls -lR /mnt/presentations
```

If the mount fails, also try `vers=2.1` or check that the Fedora host can reach the VM:

```bash
ping 192.168.122.204
```

## Files available in the share

All files are under `/mnt/presentations` with the original folder structure preserved.

| Relative path | Size (bytes) | Last modified (UTC) | Notes |
|---|---|---|---|
| `Desktop/AI-Driven Development.pdf` | 3,333,620 | 2026-06-11 | **Exact duplicate** of Documents and Downloads copies |
| `Desktop/Presentaties/AI-20251103_lenny_remix.pdf` | 5,966,850 | 2026-04-10 | PDF export of the PPTX below |
| `Desktop/Presentaties/AI-20251103_lenny_remix.pptx` | 48,246,132 | 2026-05-04 | Source presentation |
| `Desktop/Presentaties/AI-Driven Development.pptx` | 17,666,368 | 2026-05-04 | Different from the PDF of same base name |
| `Desktop/Presentaties/Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | 5,040,756 | 2026-05-04 | **Older/smaller version** |
| `Desktop/Presentaties/Moltbook_MiddagSessie.pptx` | 14,378,866 | 2026-05-04 | |
| `Desktop/Presentaties/StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | 18,016,799 | 2026-05-04 | Likely newer than "StateDD_ Een Project-OS..." |
| `Desktop/Presentaties/StateDD_ Een Project-OS voor AI Coding Agents.pptx` | 9,788,725 | 2026-05-04 | Likely older/base version |
| `Documents/AI-Driven Development.pdf` | 3,333,620 | 2026-06-11 | **Exact duplicate** |
| `Documents/Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | 30,712,362 | 2026-05-05 | **Newer/larger version** |
| `Downloads/AI-Driven Development.pdf` | 3,333,620 | 2026-06-11 | **Exact duplicate** |

## Deduplication and cleanup rules

1. **Exact duplicates** (same name, size, and modification time)
   - Keep only one copy.
   - Example: `AI-Driven Development.pdf` appears three times with identical size and timestamp.

2. **Same base name, different extension**
   - Treat `.pptx` and `.pdf` as distinct unless you can verify the PDF is a faithful export of the PPTX.
   - Example: `AI-20251103_lenny_remix.pptx` and `AI-20251103_lenny_remix.pdf` are likely related; keep both unless you confirm the PDF is a direct export.

3. **Same name, different size or timestamp**
   - Keep the **newest** (latest modification time) and largest file as the canonical version.
   - Flag the older/smaller as an obvious older version and remove it.
   - Example: `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` — keep `Documents/` copy (2026-05-05, 30 MB), remove `Desktop/Presentaties/` copy (2026-05-04, 5 MB).

4. **Version/name pattern older versions**
   - Watch for names containing `v1`, `v2`, `v3`, `old`, `draft`, `backup`, `copy`, `kopie`, etc.
   - Example: `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` vs `StateDD_ Een Project-OS voor AI Coding Agents.pptx` — inspect content if possible; if not, keep the "v2" as newer and archive/remove the older base version if it is fully superseded.

5. **Temporary/lock files**
   - Remove files starting with `~$` (Office lock/temp files). None were copied to the backup, but check the source if you expand the search.

## Suggested destination on Fedora host

```text
~/PresentationsArchive/
```

Organize final files by topic or date, or flatten into a single directory after deduplication if preferred. Document what was removed and why.

## Verification checklist

- [ ] SMB share mounts successfully.
- [ ] All 11 files are copied to the Fedora host.
- [ ] Exact duplicates of `AI-Driven Development.pdf` reduced to one copy.
- [ ] Older `Digitale dubbelgangers_...` version removed.
- [ ] Related `.pptx`/`.pdf` pairs reviewed and handled.
- [ ] Versioned/patterned older files reviewed.
- [ ] Final archive listing saved alongside files.

## Contact / context

- Windows VM user account: `lenne`
- Backup created: 2026-06-14
- Share created: `Presentations`
