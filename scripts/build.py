"""Stage only public site assets for Cloudflare Workers."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
out = root / 'dist'
if out.exists():
    shutil.rmtree(out)
out.mkdir()
for name in ('index.html', 'accessibility.css', 'accessibility.js'):
    shutil.copy2(root / name, out / name)
shutil.copy2(root / 'src/worker.js', out / '_worker.js')
(out / '_routes.json').write_text('{"version":1,"include":["/*"],"exclude":["/assets/*"]}\n')
shutil.copytree(root / 'assets', out / 'assets')
assert sorted(p.name for p in out.iterdir()) == ['_routes.json', '_worker.js', 'accessibility.css', 'accessibility.js', 'assets', 'index.html']
print(f'Staged {sum(p.is_file() for p in out.rglob("*"))} public files in {out}')
