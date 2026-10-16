# CoreWeave (CRWV) 信用風險週報

每週追蹤 CoreWeave 的信用與營運風險，產出給主管的週報。

## 結構

| 路徑 | 內容 |
|---|---|
| `framework.md` | 風險框架：七大風險面向、追蹤指標、燈號門檻 |
| `data/kpi_tracker.csv` | 每週關鍵指標（CDS、債券價格、股價、評等…），一週一列 |
| `reports/YYYY-MM-DD_週報.md` | 每週報告 |
| `templates/weekly_template.md` | 週報範本 |

## 每週流程

1. 更新 `data/kpi_tracker.csv`：新增本週一列（數據以週四收盤為準，Bloomberg / ICE / TRACE 為優先來源）。
2. 依 `framework.md` 的門檻重新評定各面向燈號，與上週比較。
3. 複製 `templates/weekly_template.md` 為 `reports/<日期>_週報.md`，先寫「一頁摘要」，再寫細節。
4. 列出下週觀察事件（財報、評等動作、新發債、大客戶消息）。

## 資料來源原則

- 財務數字以 SEC 申報（10-Q / 10-K / 8-K）為準；媒體數字若互相矛盾，報告中須註明。
- 市場數據（CDS、債券價格）以終端機報價核對後再送出。
