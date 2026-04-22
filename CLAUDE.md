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

## 當前進度快照（2026/04/22）

### 已完成主題
| 主題 | 狀態 |
|------|------|
| Hash Map / Cache Design | ✅ 全部完成 |
| Heap / Priority Queue | #703 #347 #621 完成，剩 #973 |
| Graph BFS/DFS | #733 #1971 #200 #207 完成，剩 #133 |
| Sliding Window | #643 #3 #567 完成，剩 #424 |
| Binary Search | #704 #278 #33 完成，剩 #153 |
| System Design | #232 #155 完成，剩 #208 |

### 剩餘重點題（4/22–4/23 最後兩天新題）
1. `Medium` #424 Longest Repeating Character Replacement
2. `Medium` #973 K Closest Points to Origin
3. `Medium` #133 Clone Graph
4. `Medium` #153 Find Minimum in Rotated Sorted Array
5. `Medium` #208 Implement Trie

> 4/24 起進入重刷模式，不做新題。

---

## 協作偏好

- 每次對話開始前先讀 STRATEGY.md 確認當前進度
- 修改策略前先說明要做什麼，確認後再動
- 筆記規範：每題 .md 底部加 `# 思路：...` 與 `# Time: O(?) Space: O(?)`

## 關鍵字規則

| 關鍵字 | 行為 |
|--------|------|
| `詳解` | 直接給完整解答 + 程式碼（帶繁體中文行內註解）+ 思路說明 + Time/Space，不先詢問 |
| `題目 + 檢討` | 直接讀 `test.py`，針對該題程式碼檢討：正確性、Time/Space、與最優解差距、可改進之處 |

## 程式碼風格偏好

- 避免一行寫法（list comprehension、dict comprehension），展開成多行提升可讀性
- 範例：`{i: [] for i in range(n)}` → 改用 for 迴圈展開
