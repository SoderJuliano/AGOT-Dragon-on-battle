"""Deploy all source mod files to the installed mod folder."""
import os, shutil

SRC  = r'C:\Users\Pedro\Downloads\AGOT-Dragon-on-battle-main'
DEST = r'C:\Users\Pedro\Documents\Paradox Interactive\Crusader Kings III\mod\AGOT-Dragon-on-battle-main'

copied = []
skipped = []

for root, dirs, files in os.walk(SRC):
    # Skip the 'tools' folder - not part of the mod
    rel_root = os.path.relpath(root, SRC)
    if rel_root.startswith('tools') or rel_root.startswith('.git'):
        dirs[:] = []
        continue

    for fname in files:
        src_file = os.path.join(root, fname)
        rel_path = os.path.relpath(src_file, SRC)
        dst_file = os.path.join(DEST, rel_path)

        # Create destination directory if needed
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)

        # Copy if dest doesn't exist or src is newer
        if not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)
            copied.append(rel_path + ' [NEW]')
        else:
            src_mtime = os.path.getmtime(src_file)
            dst_mtime = os.path.getmtime(dst_file)
            if src_mtime > dst_mtime:
                shutil.copy2(src_file, dst_file)
                copied.append(rel_path + ' [UPDATED]')
            else:
                skipped.append(rel_path)

if copied:
    print('DEPLOYED:')
    for p in copied:
        print(' ', p)
else:
    print('All files already up to date.')

print(f'\nSummary: {len(copied)} deployed, {len(skipped)} unchanged')
