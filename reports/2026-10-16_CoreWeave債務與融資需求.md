# CoreWeave 債務與融資需求分析（2026/10/16）

> 資料截至：2026/10/15
> 資產負債數字以 2026/6/30（Q2 10-Q）為基準；之後的發行依公司公告補上。
> 標「估算」的數字是本報告依公司指引自行推算，假設列在各節。媒體數字有互相矛盾處，送出前請以 10-Q 與 Bloomberg 核對。

## 結論

1. **債務規模：** 6/30 債務本金 356 億美元，加上租賃約 500–520 億美元。結構分兩層：
   - **專案層：** GPU／合約擔保的 DDTL，136 億美元，由客戶合約現金流攤還。
   - **公司層：** 無擔保債與可轉債 166 億美元，加上循環信用額度。
2. **發債量：** 2025 年新增債務額度約 116 億美元；2026 年截至 9 月已達約 277 億美元，是 2025 年的 2.4 倍。另有約 10 億美元私募增資。
3. **還需要融資嗎？需要，而且是持續性的。**
   - 2026 下半年的資金來源與用途大致打平，但幾乎沒有緩衝。
   - 2027 年若資本支出與 2026 年持平，估算仍需約 280–330 億美元的新融資。
4. **真正的問題不在短期到期，而在「公司層」資金管道。**
   - 專案層 DDTL 仍借得到：8 月 26 億美元超額認購，利率 SOFR+550bp。
   - 公司層無擔保債殖利率已到 15%，新發行幾乎不可行。
   - 剩下的選項是可轉債與增資，代價是股東稀釋。

## 一、債務結構（2026/6/30）

| 類別 | 本金（億美元） | 利率 | 擔保 | 說明 |
|---|---|---|---|---|
| DDTL（延遲提領定期貸款） | 136 | SOFR+225～+550bp；4.0 有約 5.9% 固定利率分券 | GPU 與客戶合約（專案層） | 依合約現金流攤還 |
| 票據（7 檔） | 166 | 無擔保 8.5–9.75%；可轉債 1.75% | 無擔保（公司層） | 包含 5 檔無擔保債、2 檔可轉債 |
| 循環信用額度 | 約 5 | 浮動 | — | 額度 25 億美元，可用 20 億美元 |
| 其他（OEM 廠商融資等） | 約 49（估算） | — | — | 總額減去上述三項 |
| **合計** | **356** | | | 加上租賃約 500–520 億美元 |

- 現金 55 億美元，總流動性（含可動用額度）156 億美元。
- 6/30 之後新增：DDTL 5.5 共 26 億美元（8 月），可轉債 37 億美元（9 月）。

### 到期分布（2026/6/30 本金）

| 年度 | 到期本金（億美元） |
|---|---|
| 2026 下半年 | 44 |
| 2027 | 62 |
| 2028–2029 | 69（估算：總額減其他年度） |
| 2030 | 32 |
| 2031 以後 | 149 |

- 2026–2027 年的到期，主要是 DDTL 依合約現金流的攤還與 OEM 融資，不是需要再融資的子彈型債券。公司在 Q1 法說會表示，2029 年前除了這兩類之外，沒有重大到期。
- 第一筆無擔保債（9.25%，20 億美元）在 2030 年 6 月才到期。

## 二、發債量

### 發行明細（2025–2026）

| 時間 | 類型 | 金額 | 利率 | 到期 | 評等／備註 |
|---|---|---|---|---|---|
| 2025/5 | 無擔保債 | 20 億美元 | 9.25% | 2030/6 | 首次發債，由 15 億上調 |
| 2025/7 | 無擔保債 | 17.5 億美元 | 9.00% | 2031/2 | 本週跌至 79.9 |
| 2025/7 | DDTL 3.0 | 26 億美元 | SOFR+400bp | 2030/8 | OpenAI 合約 |
| 2025/9 | DDTL 2.1 | 最高 30 億美元 | SOFR+425bp | — | 2026/7 起季度攤還 |
| 2025/12 | 可轉債 | 22.5 億美元 | 1.75% | 2031/12 | 由 20 億上調 |
| 2026/3 | DDTL 4.0 | 85 億美元 | SOFR+225bp／約 5.9% 固定 | 2032/3 | A3，首筆投資級 GPU 擔保融資 |
| 2026/4 | 可轉債 | 35 億美元 | 1.75% | 2032/10 | 由 30 億上調 |
| 2026/4 | 無擔保債 | 27.5 億美元 | 9.75% | 2031/10 | 17.5 億 + 10 億增發（102 發行） |
| 2026/5 | DDTL 5.0 | 31 億美元 | SOFR+450bp | 2031/11 | Ba2 / BB+ |
| 2026/6 | 無擔保債 | 12.5 億美元 | 9.625% | 2032/7 | |
| 2026/6 | 無擔保債（歐元） | 20 億歐元（約 23 億美元） | 8.50% | 2032/7 | |
| 2026/8 | DDTL 5.5 | 26 億美元 | SOFR+550bp | 約 2031 | Ba2 / BB+；合約平均僅約 3 年 |
| 2026/9 | 可轉債 | 37 億美元 | 2.875% | 2033/4 | 轉換價約 97.85 美元；另有報導稱含超額配售為 42 億 |
| 2026/9 | ATM 增資計畫 | 最多 3,500 萬股 | — | — | 以 65 美元計約 23 億美元；尚未見實際動用揭露 |

### 年度彙總（億美元，DDTL 以額度計）

| 類型 | 2025 | 2026（截至 9 月） |
|---|---|---|
| 無擔保債 | 37.5 | 63 |
| 可轉債 | 22.5 | 72 |
| DDTL | 56 | 142 |
| **合計** | **116** | **277** |

- 公司在 Q2 法說會表示，單季募集約 180 億美元（債、可轉債、股權），年初至 8 月已取得逾 320 億美元資金。這個口徑比上表廣，包含 OEM 融資、額度調整等。
- 利息負擔：Q2 淨利息費用 6.4 億美元，Q3 指引 8.6–9.4 億美元。年化約 36 億美元，相當於 2026 全年營收指引（124–132 億美元）的約 28%。

## 三、還需要融資嗎？

### 2026 下半年資金缺口（估算，億美元）

| 資金用途 | 金額 | 資金來源 | 金額 |
|---|---|---|---|
| 下半年資本支出 | 約 199（179–219） | 6/30 現金 | 55 |
| 下半年到期本金 | 44 | 6/30 未動用額度 | 約 101 |
| | | 7–9 月新融資（DDTL 5.5 + 可轉債） | 63 |
| | | 下半年營運現金流（假設與上半年相同） | 約 37 |
| **合計** | **約 243** | **合計** | **約 256** |

假設與說明：
- 下半年資本支出 = 全年指引 350–390 億美元，減去上半年 171 億美元（Q1 77 億 + Q2 94 億，權責基礎）。
- 上半年營運現金流 36.6 億美元，包含客戶預付款；公司預估 2026 年客戶預付款逾 90 億美元。
- 未動用額度多數綁定特定合約與資本支出，不能挪作他用。
- 現金不可能全部用完，公司需要保留營運現金。

**判讀：** 2026 年大致可以撐過去，但緩衝只有約 10–15 億美元，現金會降到很低的水位。這解釋了 9 月為何同時推出可轉債與 ATM。

### 2027 年（情境估算）

- 公司尚未給 2027 資本支出指引，只說會持續擴張：2030 年前再增加 5GW。
- 若 2027 資本支出與 2026 持平，約 370 億美元：
  - 加上到期本金 62 億美元；
  - 減去營運現金流，假設 100–150 億美元；
  - **仍需新融資約 280–330 億美元**，與 2026 年的發行量相當。

### 錢從哪裡來：兩層資金管道

| | 專案層（DDTL） | 公司層（無擔保債／可轉債／股權） |
|---|---|---|
| 用途 | 已簽約客戶的 GPU 與設備 | 專案層貸款不足的部分（股本份額）、資料中心、營運資金 |
| 擔保 | GPU 與客戶合約 | 無 |
| 目前成本 | SOFR+225～+550bp | 無擔保債殖利率約 15%；可轉債票息 1.75–2.875% |
| 市場狀況 | 仍開放：8 月 DDTL 5.5 超額認購 | 無擔保債困境，新發行幾乎不可行；可轉債轉換價 97.85 遠高於股價 |
| 風險 | 合約年期縮短：DDTL 5.5 合約約 3 年、貸款約 5 年 | 依賴可轉債與 ATM，股東稀釋 |

**判讀：**
- 只要有新合約，專案層借得到錢。
- 問題在公司層：每筆專案仍需要一部分股本與公司層資金。以前靠 9–9.75% 的無擔保債，現在這條路的成本變成約 15%。
- 若市場持續緊縮，公司只能用可轉債或增資填補（稀釋股東），否則就得放慢擴張。

## 四、後續觀察

| 觀察項目 | 為什麼重要 |
|---|---|
| ATM 實際動用量 | 公司層資金是否已開始依賴增資 |
| 下一筆 DDTL 的利率與條款 | 專案層管道是否也開始收緊 |
| 是否再發無擔保債，或改用有擔保結構 | 測試公司層市場是否重新打開 |
| Q3 財報（預計 11/9–11/16，未確認） | 現金餘額、Q4 資本支出、2027 初步指引 |
| S&P／Moody's 評等 | 市場價格已低於評等，調降機率上升 |
| 超大雲端業者 10 月下旬財報 | 需求端是否支撐 CoreWeave 的新合約 |

## 資料來源

- [CoreWeave 10-Q（2026 Q2）](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm)
- [CoreWeave 10-Q（2026 Q1）](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000222/crwv-20260331.htm)
- [CoreWeave Q2 2026 法說會逐字稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CRWV-US-CORRECTED-TRANSCRIPT-CoreWeave-Q2-2026-Earnings-Call-11August2026.pdf)
- [StockTitan：CoreWeave 與 Nebius 債務到期分布](https://www.stocktitan.net/articles/coreweave-nebius-ai-cloud-debt-when-it-comes-due)
- [Forbes：CoreWeave bonds are warning of a bigger problem](https://www.forbes.com/sites/jimosman/2026/10/14/coreweave-bonds-are-warning-of-a-bigger-problem-for-ai-stocks/)
- [Fenwick：2030 年到期 20 億美元無擔保債](https://www.fenwick.com/insights/experience/fenwick-represents-coreweave-in-upsized-2-billion-offering-of-senior-notes-due-2030)
- [CoreWeave IR：2031 年 9.00% 無擔保債 17.5 億美元](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Announces-Closing-of-1750-million-of-Senior-Notes-Offering/default.aspx)
- [CoreWeave IR：2031 年 9.75% 無擔保債增發 10 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Pricing-of-1000-million-of-9-750-Senior-Notes-due-2031/default.aspx)
- [CoreWeave IR：12.5 億美元與 20 億歐元 2032 年無擔保債](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Pricing-of-1-25-Billion-of-Senior-Notes-and-2-Billion-of-Senior-Notes/default.aspx)
- [Business Wire：2031 年可轉債 22.5 億美元](https://www.businesswire.com/news/home/20251209164014/en/CoreWeave-Prices-Upsized-%242.25-Billion-Convertible-Senior-Notes-Offering)
- [CoreWeave IR：2032 年可轉債 35 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-5-Billion-Convertible-Senior-Notes-Offering/default.aspx)
- [CoreWeave IR：2033 年可轉債 37 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx)
- [CoreWeave IR：DDTL 4.0 共 85 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-Landmark-8-5-Billion-Financing-Facility-Achieving-First-Investment-Grade-Rated-GPU-backed-Financing/default.aspx)
- [CoreWeave IR：DDTL 5.0 共 31 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-3-1-Billion-Loan-Facility-Expanding-Access-to-Public-Markets-for-GPU-Backed-Financing/default.aspx)
- [CoreWeave IR：DDTL 5.5 共 26 億美元](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx)
- [CoreWeave IR：DDTL 3.0（2025）](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Closes-2-6-Billion-Secured-Debt-Financing-Facility-Strengthening-Market-Position-as-AI-Cloud-Leader/default.aspx)
- [CoreWeave 委託書（DDTL 2.0／2.1）](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000191/crwv-20260422.htm)
- [24/7 Wall St.：Q2 2026 自由現金流](https://247wallst.com/cards/coreweave-inc-q2-2026-earnings-crwv-01kzs7w6z6463rene3akq02dn2)
- [Futurum：Q1 2026 資本支出](https://futurumgroup.com/insights/coreweave-q1-fy-2026-capacity-constraints-amid-accelerating-ai-demand/)
- [Motley Fool：9 月可轉債與 ATM](https://www.fool.com/investing/2026/09/17/why-coreweave-stock-dived-by-more-than-5-today/)
- [Bloomberg Law：CDS 隱含 60% 違約機率](https://news.bloomberglaw.com/business-and-practice/coreweave-risk-gauge-hits-record-pricing-60-odds-of-default)
