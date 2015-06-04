

023 Merge k Sorted Lists
-------------------------------
提交的结果里python是最快的。
c实现的heapsort大概400ms.
python内置的timsort非常快,100ms.


078 Subsets
-------------------------------
数据坑。
题目要求输出的元素必须是以不下降顺序，
不是指按照输入元素的不下降输出，而是数字大小不下降。
要先排个序。


052 N-Queens II
-------------------
搜索算法O(N!), N不可能很大。
一个用位操作的写法，非常高效。


010 Regular Expression Matching
-------------------------------
构造一个简化的DFA
我的代码在Input="aaa","aaa"下，OJ返回false。而在gcc下是true。
不知哪里错了。


079 WordSearch
--------------------
Wrong Answer in c.



140 Word Break II
---------------------
有一个很恶心的测试数据 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

从左到右，DFS 搜索肯定不行。
从左到右，按位划分阶段，Phase(i) 表示从0~i的结果集，做DP， 最后一位b到最后才会检测出来，导致时间和内存爆掉。
从左到右，按位划分阶段，Phase(i)表示i~end的结果集。但是用递归来带动阶段前进，共享结果空间来DP，而不是按照阶段一个一个做。优点a) 可以跳过数据中没有涉及到的阶段 b) 很快检测到最后一位 c)实现起来更直观，是递推公式的直接表达。
从右往左递归，可能更符合递推公式。
