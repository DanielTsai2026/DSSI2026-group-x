"""完全虛構的資料夾流程示範；不是商業實際資料。Python 標準函式庫即可執行。
從專案根目錄執行：python data/code/demo_generate_orders.py
依固定公式生成 120 筆訂單，注入 3 個數量缺值、2 個負單價與 2 筆完整重複。
既有檔案只有內容完全相同時才接受；不同內容不覆寫。
"""
from pathlib import Path
import csv
import io
import hashlib
root = Path(__file__).resolve().parents[2]
assert (root / 'AGENTS.md').is_file() and (root / 'templates').is_dir()
rows = []
for i in range(120):
    category = ['A', 'B', 'C'][i % 3]
    rows.append({
        'order_id': f'D{i+1:04d}',
        'order_date': f'2026-09-{i % 30 + 1:02d}',
        'category': f' {category} ' if i % 11 == 0 else category,
        'quantity': '' if i in [8, 48, 88] else (i * 7) % 5 + 1,
        'unit_price_twd': -100 if i in [19, 79] else 80 + (i * 17) % 221,
    })
rows.extend([rows[0].copy(), rows[1].copy()])
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
payload = buffer.getvalue().encode('utf-8')
path = root / 'data/raw/demo_orders.csv'
path.parent.mkdir(parents=True, exist_ok=True)
if path.exists():
    if path.read_bytes() != payload:
        raise FileExistsError('既有示範原始檔內容不同，停止以保留原檔。')
else:
    with path.open('xb') as stream:
        stream.write(payload)
print({'path': 'data/raw/demo_orders.csv', 'rows': len(rows), 'sha256': hashlib.sha256(payload).hexdigest()})
