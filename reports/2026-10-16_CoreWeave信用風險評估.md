# CoreWeave 信用風險評估（2026/10/16）

> 資料截至：2026/10/15
> ⚠️ 本報告數字來自媒體報導（Bloomberg、CNBC、Forbes 等），部分來源互相矛盾，送出前請以 Bloomberg 終端機核對 CDS、債券報價與評等。

## 一頁摘要

**結論：CoreWeave 的信用指標本週進入困境區間。5 年期 CDS 一週內從 368bp 跳到 1,194.5bp（歷史新高），隱含 5 年違約機率約 60%；無擔保債跌破 80 美分，殖利率超過 15%。基本面（backlog 1,042 億美元）沒有變壞，但公司的成長完全依賴持續融資，而市場現在正在質疑的就是這個融資管道。**

| 風險面向 | 燈號 | 一句話 |
|---|---|---|
| 1. 市場隱含信用風險 | 🔴 | CDS 1,194.5bp，債價 < 80，殖利率 > 15%，全部超過困境門檻 |
| 2. 再融資與流動性 | 🟠 | 短期到期可應付；問題是 2026 年 350–390 億美元的資本支出必須持續靠外部融資 |
| 3. 獲利與償債能力 | 🔴 | Q2 淨損 6.26 億美元；Q3 利息費用指引 8.6–9.4 億美元，比 Q2 高約 40% |
| 4. 客戶集中與交易對手 | 🟠 | 前兩大客戶約占營收 65%；曝險正從 Microsoft 移向 OpenAI 和 Meta |
| 5. 執行與交付 | 🟡 | 全年營收指引集中在下半年，Q3 財報是第一個檢驗點 |
| 6. 擔保品與技術折舊 | 🟡 | GPU 擔保貸款 136 億美元；貸款約 5 年，客戶合約平均約 3 年 |
| 7. 傳染與系統風險 | 🟠 | Nebius、Oracle 同步下跌；市場已把 CoreWeave 當作 AI 信貸的指標股 |

**關鍵數字：**

| 指標 | 本週 | 上週 | 變化 |
|---|---|---|---|
| 5Y CDS | 1,194.5bp（10/15 盤中高點） | 643bp（10/9） | +551bp；10/6 時僅 368bp |
| 隱含 5 年違約機率 | 約 60–63% | 約 41% | 回收率假設 40% |
| 2031 年 9% 無擔保債 | 79.9 / 殖利率 15.6% | — | 單日跌 3.3 美分 |
| 股價 | 10/14 收 65.78 美元；10/15 反彈 +5.94% | — | 四個交易日市值蒸發超過 100 億美元 |
| 評等 | S&P B+；Moody's Ba3（待核對） | — | 無變動 |

## 本週重大事件

1. **10/14（三）債券重挫**：2031、2032 年到期無擔保債跌破 80 美分，殖利率超過 15%。股價盤中一度跌超過 15%。Elon Musk、Chamath Palihapitiya 在社群媒體上評論，放大了市場關注。Chamath 稱 AI 是「私募信貸泡沫」。
2. **10/15（四）CDS 創新高**：ICE 數據顯示 5Y CDS 盤中達 1,194.5bp。
3. **10/15 反彈**：Nvidia 執行長黃仁勳在斯德哥爾摩表示 CoreWeave「不需要紓困（backstop）」，並說它的資金成本正在下降。Deutsche Bank 維持買進，目標價 150 美元，稱這次下跌是「買進機會」。ARK（Cathie Wood）買進約 1,340 萬美元股票。股價收漲 5.94%。
4. **公司回應**：CEO Mike Intrator 發內部信，稱市場反應「不理性」，並以 1,042 億美元 backlog 安撫員工。公司表示 backlog「足以支應所有債務」。
5. **沒有單一觸發事件**：媒體找不到本週新的融資公告。賣壓來自市場對 AI 公司舉債規模的整體疑慮。9 月的 37 億美元可轉債和 3,500 萬股 ATM 計畫，本週再度被拿出來討論。

## 各面向分析

### 1. 市場隱含信用風險 🔴

- CDS 在 7 個交易日內從 368bp 漲到 1,194.5bp，漲幅超過 3 倍。1,000bp 一般被視為困境門檻。
- 隱含違約機率：1,194.5 ÷ (1 − 40%) ≈ 年違約率 19.9%，5 年累積約 63%。7 月底時約 50%。
- 2031 年 9% 債跌到 79.9，殖利率 15.6%（TRACE）；另一檔 2031 年 9.75% 債約 78.65。
- **解讀**：這是市場定價，不是評等。S&P B+ / Moody's Ba3 是「投機級但非困境」，而市場價格已經落在 CCC 區間。兩者差距這麼大時，評等機構接下來調降評等的機率會上升。

### 2. 再融資與流動性 🟠

| 項目 | 金額（2026/6/30） |
|---|---|
| 債務本金 | 356 億美元（含租賃等義務約 500–520 億美元） |
| 2026 下半年到期 | 44 億美元 |
| 2027 年到期 | 62 億美元 |
| 現金 | 55 億美元 |
| 總流動性（含可動用額度） | 156 億美元 |
| 2026 全年資本支出指引 | 350–390 億美元（8 月上調） |

- 9 月發行 2.875% 可轉債（2033 年到期），定價 37 億美元。有報導指加計超額配售後為 42 億美元，待核對。轉換價約 97.85 美元。另外設立最多 3,500 萬股的 ATM 計畫。
- **短期不是問題**：156 億美元流動性足以應付 2027 年底前約 106 億美元的到期本金。
- **真正的風險**：資本支出遠大於營運現金流，缺口要靠每季持續發債、發可轉債或增資來補。融資成本若停留在 15%，或市場關門，擴張計畫就得減速，backlog 的交付也會跟著受影響。
- 股價跌到 65 美元附近，離可轉債轉換價（97.85）很遠，可轉債實質上更像純債務。

### 3. 獲利與償債能力 🔴

- Q2 淨損 6.26 億美元，Q2 淨利息費用 6.4 億美元。
- Q3 利息費用指引 8.6–9.4 億美元，比 Q2 增加約 40%，反映持續舉債。
- 全年營收指引 124–132 億美元。上半年 46.8 億美元，代表下半年須達到 76–80 億美元，比上半年多約 65%。
- 有分析師指出，公司借款成本約 9%，資本報酬率卻只有約 1%。這組數字待核對，但方向值得注意。

### 4. 客戶集中與交易對手 🟠

- 2025 全年：Microsoft 約占營收 67%。
- 2026 Q1（10-Q）：前兩大客戶合計約 65%，其他客戶均不到 10%。
- 新合約分散了客戶結構：Meta（3 月簽約約 210 億美元）、OpenAI，以及 Anthropic、Google。
- **二階風險**：曝險正從 Microsoft（AAA）移向 OpenAI（非投資等級、仍在燒錢）。backlog 的信用品質取決於這些客戶本身的付款能力。

### 5. 執行與交付 🟡

- 目標：2026 年底上線電力 1.7GW。SemiAnalysis 認為大部分廠址進度正常。
- 前例：2025 年 Q3 曾因第三方開發商延遲而下修營收，之後修改了貸款契約，延後部分財務條款的測試時間。
- Backlog 中超過 50% 已開始交付，管理層預期年底超過三分之二。
- Q3 財報是檢驗下半年營收能否達標的第一個時間點。

### 6. 擔保品與技術折舊 🟡

- 356 億美元債務中，GPU 擔保的專案貸款占 136 億美元，是最大的一類。
- 8 月的 26 億美元貸款利率為 SOFR + 550bp，年期約 5 年；客戶合約平均約 3 年，有期限錯配。
- GPU 世代更替很快。合約到期後若無法續約，擔保品的殘值就是貸款人的關鍵風險。

### 7. 傳染與系統風險 🟠

- Nebius 10/14 收在 186.01 美元，跌破 200 美元；Oracle 同步走弱。
- 市場已把 CoreWeave 當作「AI 資料中心債務」的代表。它的債價會影響整個 AI 基礎建設融資的成本。
- 本月底超大雲端業者公布財報，資本支出指引將決定市場情緒方向。

## 支撐因素（反方觀點）

- **Backlog 1,042 億美元**，年增約 246%，Q3 初又新增超過 250 億美元。多為 take-or-pay 長約。
- **Nvidia 的隱性支撐**：持股約 20 億美元，並承諾在 2032 年前買下最多 63 億美元的閒置產能。黃仁勳說「不需要紓困」，但這些既有承諾本身已經是一種部分支撐。
- **賣方多數偏多**：Deutsche Bank 買進（目標價 150 美元）；Wedbush 的 Dan Ives 稱賣壓「過度」。Bernstein 則維持「表現落後大盤」，稱其商業模式「經濟上有挑戰」。
- **短期沒有到期牆**：2027 年底前的到期本金低於現有流動性。

## 後續觀察事件

| 時間 | 事件 | 為什麼重要 |
|---|---|---|
| 10 月下旬 | Microsoft、Meta、Google、Amazon 財報 | 資本支出指引若維持或上調，可緩解市場疑慮 |
| 持續 | CDS 是否回落到 1,000bp 以下 | 判斷本週是恐慌還是重新定價 |
| 持續 | S&P / Moody's 評等動作 | 市場價格與評等差距大，負面展望或調降的機率上升 |
| 持續 | ATM 實際動用、新的發債或貸款 | 融資條件（利率、條款）是最直接的訊號 |
| 11/9–11/16（未確認） | Q3 財報 | Q3 營收指引 34–36 億美元，市場預估約 35.4 億美元；下半年能否達標 |

## 資料來源

- [Bloomberg：CoreWeave Bonds Plunge to Distress Levels](https://www.bloomberg.com/news/articles/2026-10-14/coreweave-bonds-tumble-into-distress-drawing-yikes-from-musk)
- [Bloomberg：Deutsche Bank says selloff is buying opportunity](https://www.bloomberg.com/news/articles/2026-10-15/coreweave-s-selloff-is-buying-opportunity-deutsche-bank-says)
- [Bloomberg：Nvidia CEO downplays CoreWeave concerns](https://www.bloomberg.com/news/articles/2026-10-15/nvidia-ceo-huang-says-coreweave-improving-no-backstop-needed)
- [Bloomberg Law：CoreWeave risk gauge hits record, pricing 60% odds of default](https://news.bloomberglaw.com/business-and-practice/coreweave-risk-gauge-hits-record-pricing-60-odds-of-default)
- [CNBC：CDS hit distress levels](https://www.cnbc.com/2026/10/15/coreweave-credit-default-swaps-hit-distress-levels-as-investors-sour-on-ai-debt.html)
- [CNBC：Bond yields near 15%](https://www.cnbc.com/2026/10/14/coreweave-stock-bond-yields-ai-debt.html)
- [Forbes：CoreWeave bonds are warning of a bigger problem](https://www.forbes.com/sites/jimosman/2026/10/14/coreweave-bonds-are-warning-of-a-bigger-problem-for-ai-stocks/)
- [Axios：CoreWeave raises warning flag for the AI trade](https://www.axios.com/2026/10/15/ai-coreweave-bonds-stocks)
- [Yahoo Finance：CoreWeave's AI bonds tumble](https://finance.yahoo.com/markets/options/articles/coreweave-ai-bonds-tumble-raising-111700097.html)
- [TheStreet：Nebius breaks below $200](https://www.thestreet.com/investing/nebius-nbis-stock-selloff-coreweave-bond-scare)
- [The Next Web：Huang says CoreWeave needs no backstop](https://thenextweb.com/news/huang-coreweave-backstop-stockholm)
- [Benzinga：Dan Ives calls selloff overdone](https://www.benzinga.com/markets/equities/26/10/62374008/dan-ives-calls-coreweave-selloff-way-overdone-says-hyperscaler-earnings-will-back-ai-spending-crwv-stock-plunges-near-12-month-low)
- [CoreWeave IR：$3.7B convertible notes pricing](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx)
- [CoreWeave 10-Q（2026 Q2）](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm)
- [CoreWeave 10-Q（2026 Q1）](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000222/crwv-20260331.htm)
- [CNBC：Q2 2026 earnings](https://www.cnbc.com/2026/08/11/coreweave-crwv-q2-earnings-report-2026.html)
- [StockTitan：CoreWeave and Nebius debt maturities](https://www.stocktitan.net/articles/coreweave-nebius-ai-cloud-debt-when-it-comes-due)
- [SemiAnalysis：data center capacity](https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter)
