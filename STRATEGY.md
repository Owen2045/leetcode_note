# 刷題策略（2026/04/15 擬定）

目標：台灣後端工程師職缺（Python / 微服務 / 快取 / 高併發）
語言：Python
來源：LeetCode 高頻題（不限 Top Interview 150）
難度配比：Easy : Medium ≈ 6 : 4（每個主題先用 Easy 熱身鞏固概念，再接 Medium）

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
- [x] #146 LRU Cache `Medium`
- [x] #242 Valid Anagram `Easy`
- [ ] #383 Ransom Note `Easy`

### Heap / Priority Queue
- [x] #703 Kth Largest Element in a Stream `Easy`
- [x] #347 Top K Frequent Elements `Medium`
- [x] #621 Task Scheduler `Medium`
- [ ] #973 K Closest Points to Origin `Medium`

### Graph BFS/DFS
- [x] #733 Flood Fill `Easy`
- [x] #1971 Find if Path Exists in Graph `Easy`
- [ ] #200 Number of Islands `Medium`
- [ ] #207 Course Schedule `Medium`
- [ ] #133 Clone Graph `Medium`

### Sliding Window
- [x] #643 Maximum Average Subarray I `Easy`
- [ ] #3   Longest Substring Without Repeating Characters `Medium`
- [ ] #424 Longest Repeating Character Replacement `Medium`
- [x] #567 Permutation in String `Medium`

### Binary Search
- [x] #704 Binary Search `Easy`
- [x] #278 First Bad Version `Easy`
- [x] #33  Search in Rotated Sorted Array `Medium`
- [ ] #153 Find Minimum in Rotated Sorted Array `Medium`

### System Design
- [x] #232 Implement Queue using Stacks `Easy`
- [x] #155 Min Stack `Medium`
- [ ] #208 Implement Trie `Medium`

### DP（備用，JD 未強調，時間不夠可跳過）
- [x] #70  Climbing Stairs `Easy`
- [ ] #746 Min Cost Climbing Stairs `Easy`
- [ ] #338 Counting Bits `Easy`
- [ ] #322 Coin Change `Medium`
- [ ] #300 Longest Increasing Subsequence `Medium`

---

## 筆記規範（每題 .md 底部務必加）

```
# 思路：...
# Time: O(?)  Space: O(?)
```

---

## 刷題流程（每題標準 SOP）

```
1. 閱讀題目（5 min）
2. 計時作答：Easy 20 min / Medium 35 min
3. 時間到仍未解出 → 直接看解答，理解思路
4. 關掉解答，從頭默寫一遍（不可略過此步）
5. 記錄思路 + Time/Space Complexity
```

> 重點：面試有時間壓力，練習目標是「時限內產出可用解」，不是無限磨到最優解。

---

## Re-attempt 規則

### 一般模式
- 初次解完後，**隔 3 天**再做一次（不看解答）
- 還是做不出來 → 再等 7 天

### 衝刺模式（面試前 2 週內）
- 初次解完後，**隔 1 天**複習
- 最後 2–3 天不做新題，只重刷做不出來或默寫卡住的題

---

目標：Easy 20 分鐘、Medium 35 分鐘內寫出乾淨解法

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
| 2026/04/15 | #217 | Contains Duplicate | Easy | |
| 2026/04/15 | #49  | Group Anagrams | Medium | |
| 2026/04/16 | #146 | LRU Cache | Medium | |
| 2026/04/16 | #703 | Kth Largest Element in a Stream | Easy | |
| 2026/04/16 | #733 | Flood Fill | Easy | |
| 2026/04/16 | #704 | Binary Search | Easy | |
| 2026/04/16 | #347 | Top K Frequent Elements | Medium | |
| 2026/04/16 | #643 | Maximum Average Subarray I | Easy | |
| 2026/04/16 | #155 | Min Stack | Medium | |

---

## 下一步建議順序（Easy:Medium ≈ 6:4）

1.  `Easy`   [#703 Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)（Heap 熱身）
2.  `Easy`   [#733 Flood Fill](https://leetcode.com/problems/flood-fill/)（Graph BFS 熱身）
3.  `Easy`   [#704 Binary Search](https://leetcode.com/problems/binary-search/)（Binary Search 熱身）
4.  `Medium` [#347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)（Heap）
5.  `Easy`   [#643 Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)（Sliding Window 熱身）
6.  `Easy`   [#242 Valid Anagram](https://leetcode.com/problems/valid-anagram/)（Hash Map 複習）
7.  `Easy`   [#1971 Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)（Graph）
8.  `Medium` [#621 Task Scheduler](https://leetcode.com/problems/task-scheduler/)（Heap，對應 Celery）
9.  `Easy`   [#278 First Bad Version](https://leetcode.com/problems/first-bad-version/)（Binary Search）
10. `Medium` [#200 Number of Islands](https://leetcode.com/problems/number-of-islands/)（Graph BFS/DFS）
11. `Easy`   [#232 Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)（System Design 熱身）
12. `Medium` [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)（Sliding Window）
13. `Medium` [#207 Course Schedule](https://leetcode.com/problems/course-schedule/)（拓樸排序，對應微服務依賴）
14. `Medium` [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Sliding Window）
15. `Medium` [#973 K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)（Heap）
16. `Easy`   [#383 Ransom Note](https://leetcode.com/problems/ransom-note/)（Hash Map）
17. `Medium` [#155 Min Stack](https://leetcode.com/problems/min-stack/)（System Design）
18. `Medium` [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/)（Sliding Window）
19. `Medium` [#33 Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)（Binary Search）
20. `Medium` [#133 Clone Graph](https://leetcode.com/problems/clone-graph/)（Graph）
21. `Medium` [#153 Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)（Binary Search）
22. `Medium` [#208 Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)（System Design，對應搜尋優化）
