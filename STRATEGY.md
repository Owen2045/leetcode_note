# 刷題策略（2026/04/15 擬定）

目標：台灣後端工程師職缺（Python / 微服務 / 快取 / 高併發）
語言：Python
來源：LeetCode 高頻題（不限 Top Interview 150）

---

## 題型優先級（對應職缺需求）

| 優先級 | 主題 | 對應 JD |
|--------|------|---------|
| ★★★ | Hash Map / Cache Design | Redis 快取、LRU 設計 |
| ★★★ | Heap / Priority Queue | Task Queue、Celery 排程 |
| ★★★ | Graph BFS/DFS | 微服務依賴、拓樸排序 |
| ★★★ | Sliding Window | 高併發資料流、效能優化 |
| ★★  | Binary Search | 高效查詢 |
| ★★  | System Design 題 | API 設計、資料結構設計 |
| ★★  | Dynamic Programming | 最佳化問題 |
| ★   | Tree | Graph 的基礎 |

---

## 每週輪換節奏

```
Mon/Tue - Hash Map / Cache Design
Wed     - Heap / Priority Queue
Thu/Fri - Graph BFS/DFS
Sat     - Sliding Window / Binary Search
Sun     - 複習本週最弱的一題（re-attempt，不看解答）
```

---

## 必練高頻清單

### Hash Map & Cache Design
- [x] #217 Contains Duplicate `Easy`
- [x] #49  Group Anagrams `Medium`
- [x] #380 Insert Delete GetRandom O(1) `Medium`
- [ ] #146 LRU Cache `Medium`

### Heap / Priority Queue
- [ ] #347 Top K Frequent Elements `Medium`
- [ ] #621 Task Scheduler `Medium`
- [ ] #973 K Closest Points to Origin `Medium`

### Graph BFS/DFS
- [ ] #200 Number of Islands `Medium`
- [ ] #207 Course Schedule `Medium`
- [ ] #133 Clone Graph `Medium`

### Sliding Window
- [ ] #3   Longest Substring Without Repeating Characters `Medium`
- [ ] #424 Longest Repeating Character Replacement `Medium`
- [ ] #567 Permutation in String `Medium`

### Binary Search
- [ ] #33  Search in Rotated Sorted Array `Medium`
- [ ] #153 Find Minimum in Rotated Sorted Array `Medium`

### System Design
- [ ] #155 Min Stack `Medium`
- [ ] #208 Implement Trie `Medium`

### DP
- [ ] #70  Climbing Stairs `Easy`
- [ ] #322 Coin Change `Medium`
- [ ] #300 Longest Increasing Subsequence `Medium`

---

## 筆記規範（每題 .md 底部務必加）

```
# 思路：...
# Time: O(?)  Space: O(?)
```

---

## Re-attempt 規則

- 初次解完後，**隔 3 天**再做一次（不看解答）
- 還是做不出來 → 再等 7 天
- 目標：Easy 20 分鐘、Medium 35 分鐘內寫出乾淨解法

---

## 進度紀錄

| 日期 | 題號 | 題目 | 難度 | 備註 |
|------|------|------|------|------|
| 2026/01/27 | #1   | Two Sum | Easy | |
| 2026/01/27 | #9   | Palindrome Number | Easy | |
| 2026/01/30 | #13  | Roman to Integer | Easy | |
| 2026/02/02 | #14  | Longest Common Prefix | Easy | |
| 2026/02/02 | #20  | Valid Parentheses | Easy | |
| 2026/02/03 | #26  | Remove Duplicates from Sorted Array | Easy | |
| 2026/02/04 | #28  | Find the Index of the First Occurrence in a String | Easy | |
| 2026/02/04 | #35  | Search Insert Position | Easy | |
| 2026/02/04 | #58  | Length of Last Word | Easy | |
| 2026/02/04 | #88  | Merge Sorted Array | Easy | |
| 2026/02/05 | #27  | Remove Element | Easy | |
| 2026/02/05 | #80  | Remove Duplicates from Sorted Array II | Medium | |
| 2026/02/05 | #169 | Majority Element | Easy | |
| 2026/02/05 | #189 | Rotate Array | Medium | |
| 2026/02/05 | #121 | Best Time to Buy and Sell Stock | Easy | |
| 2026/02/09 | #45  | Jump Game II | Medium | |
| 2026/02/09 | #274 | H-Index | Medium | |
| 2026/02/09 | #380 | Insert Delete GetRandom O(1) | Medium | |
| 2026/02/09 | #238 | Product of Array Except Self | Medium | |
| 2026/02/09 | #134 | Gas Station | Medium | |

---

## 下一步建議順序

1. [#146 LRU Cache](https://leetcode.com/problems/lru-cache/)（Cache Design，對應 Redis）
2. [#347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)（Heap 入門）
3. [#621 Task Scheduler](https://leetcode.com/problems/task-scheduler/)（Heap，對應 Celery）
4. [#200 Number of Islands](https://leetcode.com/problems/number-of-islands/)（Graph BFS/DFS 入門）
5. [#207 Course Schedule](https://leetcode.com/problems/course-schedule/)（拓樸排序，對應微服務依賴）
6. [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)（Sliding Window 入門）
