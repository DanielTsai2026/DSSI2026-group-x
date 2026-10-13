"""產生訂單、商品類別及日期三份練習資料。
執行方式：python data/code/demo_generate_orders.py
"""
from pathlib import Path
from datetime import date
import csv

root = Path(__file__).resolve().parents[2]
raw_dir = root / "data/raw"
raw_dir.mkdir(parents=True, exist_ok=True)

orders = []
for i in range(120):
    category = ["A", "B", "C"][i % 3]
    orders.append({
        "order_id": f"D{i+1:04d}",
        "order_date": f"2026-09-{i % 30 + 1:02d}",
        "category": f" {category} " if i % 11 == 0 else category,
        "quantity": "" if i in [8, 48, 88] else (i * 7) % 5 + 1,
        "unit_price_twd": -100 if i in [19, 79] else 80 + (i * 17) % 221,
    })

# 加入兩筆重複資料，留給後面的清理練習。
orders.extend([orders[0].copy(), orders[1].copy()])
categories = [
    {"category": "A", "category_name": "飲品"},
    {"category": "B", "category_name": "點心"},
    {"category": "C", "category_name": "輕食"},
]

weekday_names = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
calendar = []
for day in range(1, 31):
    order_date = date(2026, 9, day)
    calendar.append({
        "order_date": order_date.isoformat(),
        "weekday": weekday_names[order_date.weekday()],
        "day_type": "週末" if order_date.weekday() >= 5 else "平日",
    })

for filename, rows in [
    ("demo_orders.csv", orders),
    ("demo_categories.csv", categories),
    ("demo_calendar.csv", calendar),
]:
    path = raw_dir / filename
    if path.exists():
        print(f"{filename} 已存在，保留原檔。")
        continue
    with path.open("x", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"已建立 {filename}，共 {len(rows)} 列。")
