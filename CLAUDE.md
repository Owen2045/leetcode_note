# Claude Code — 專案記憶

此檔案由 Claude Code 自動讀取，換裝置後透過 git 同步即可還原 context。

---

## 使用者背景

- 目標職缺：**ASUS AD10601 Senior Python Backend Engineer**
- 面試截止日：**2026/04/27**
- 刷題語言：Python
- 刷題紀錄與策略詳見 [STRATEGY.md](STRATEGY.md)

### JD 核心技術對照

| 技術 | 對應題型 |
|------|---------|
| Redis 快取 | Hash Map / LRU Cache Design |
| Celery / Task Queue | Heap / Priority Queue |
| 微服務依賴 | Graph BFS/DFS、拓樸排序 |
| 高併發資料流 | Sliding Window |
| 高效查詢 | Binary Search |
| GenAI / LangChain / RAG | 面試口頭補充，非刷題範圍 |

---

## 刷題策略摘要

- 難度配比：**Easy : Medium ≈ 6 : 4**
- 題型優先級：Hash Map / Heap / Graph / Sliding Window > Binary Search / System Design > DP（備用）
- DP 未在 JD 強調，時間不夠可跳過

### 每題 SOP

```
1. 閱讀題目（5 min）
2. 計時作答：Easy 20 min / Medium 35 min
3. 時間到仍未解出 → 直接看解答，理解思路
4. 關掉解答，從頭默寫一遍（不可略過）
5. 記錄思路 + Time/Space Complexity
```

### 11 天衝刺節奏（2026/04/16–04/27）

| 天數 | 內容 |
|------|------|
| Day 1–8（04/16–04/23） | 每天 2 題，照「下一步建議順序」推進 |
| Day 9–10（04/24–04/25） | 不做新題，重刷做不出來或默寫卡住的題 |
| Day 11（04/26） | 輕量複習，確認每題 Time/Space 能口頭說出來 |

---

## 協作偏好

- 每次對話開始前先讀 STRATEGY.md 確認當前進度
- 修改策略前先說明要做什麼，確認後再動
- 筆記規範：每題 .md 底部加 `# 思路：...` 與 `# Time: O(?) Space: O(?)`
