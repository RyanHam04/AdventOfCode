## Progress of Advent of Code

Author: Ryan Ham, Bsc. Artificial Intelligence Student at the University of Groningen,

### Summary Table

| Day   | Stars | Tries Part 1 | Tries Part 2 | Time Complexity                                      | Evaluation                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | ----- | ------------ | ------------ | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Day 1 | ⭐⭐  | 1            | 1            | O(n<sup>2</sup>)                                     | Regarding time complexity, it could have been improved by using "Counter()" for instant lookup. It uses O(n) time to build the dictionary. Placing this outside of the for-loop would decrease the time complexity to O(n)                                                                                                                                                                                                                                        |
| Day 2 | ⭐⭐  | 1            | 3            | O(m \* n<sup>2</sup>)                                | The overall time complexity of part 2 is O(m \* n<sup>2</sup>), m being the number of lines and n the amount of items per list. Up until now I have not found significant optimizations                                                                                                                                                                                                                                                                           |
| Day 3 | ⭐⭐  | 1            | 1            | O(n)                                                 | Regex.findall() uses approximately O(n), for now I have not found a better way.                                                                                                                                                                                                                                                                                                                                                                                   |
| Day 4 | ⭐⭐  | 1            | 1            | O(m\*n) - m = rows, n = cols                         | For part 1, the use of NumPy-arrays seemed intuitive, since it can rotate the matrices which is really helpful. However this made me blind for the fact that they are less practical for the second part, this caused some additional (unnecessary) troubles. I saw this as a challenge to learn more about NumPy arrays and decided to proceed with this approach. This assignment was the toughest up until now, probably even without the use of numpy arrays. |
| Day 5 | ⭐⭐  | 1            | 1            | Part 1 O(n \* m), </br> Part 2 O(n<sup>2</sup> \* m) | m = rules, n = len(update) \* updates -- I found these assignments more straightforward than yesterday. For part 2 updating works recursively. This is in my opinion most intuitive, which made it easy to work with.                                                                                                                                                                                                                                             |

### Performance

| **Day**   | **Part 1 Time** | **Part 1 Rank** | **Part 1 Score** | **Part 2 Time** | **Part 2 Rank** | **Part 2 Score** |
| --------- | --------------- | --------------- | ---------------- | --------------- | --------------- | ---------------- |
| **Day 5** | 07:03:08        | 37,326          | 0                | 07:19:37        | 29,538          | 0                |
| **Day 4** | 11:34:52        | 55,147          | 0                | 16:56:38        | 64,002          | 0                |
| **Day 3** | 08:36:04        | 59,704          | 0                | 09:00:51        | 50,653          | 0                |
| **Day 2** | 05:09:36        | 42,106          | 0                | 08:39:48        | 41,490          | 0                |
| **Day 1** | 10:51:15        | 58,565          | 0                | 11:18:30        | 56,034          | 0                |

---
