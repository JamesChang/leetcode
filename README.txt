

023 Merge k Sorted Lists
-------------------------------
�ύ�Ľ����python�����ġ�
cʵ�ֵ�heapsort���400ms.
python���õ�timsort�ǳ���,100ms.


078 Subsets
-------------------------------
���ݿӡ�
��ĿҪ�������Ԫ�ر������Բ��½�˳��
����ָ��������Ԫ�صĲ��½�������������ִ�С���½���
Ҫ���Ÿ���


052 N-Queens II
-------------------
�����㷨O(N!), N�����ܴܺ�
һ����λ������д�����ǳ���Ч��


010 Regular Expression Matching
-------------------------------
����һ���򻯵�DFA
�ҵĴ�����Input="aaa","aaa"�£�OJ����false������gcc����true��
��֪������ˡ�


079 WordSearch
--------------------
Wrong Answer in c.



140 Word Break II
---------------------
��һ���ܶ��ĵĲ������� "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

�����ң�DFS �����϶����С�
�����ң���λ���ֽ׶Σ�Phase(i) ��ʾ��0~i�Ľ��������DP�� ���һλb�����Ż������������ʱ����ڴ汬����
�����ң���λ���ֽ׶Σ�Phase(i)��ʾi~end�Ľ�����������õݹ��������׶�ǰ�����������ռ���DP�������ǰ��ս׶�һ��һ�������ŵ�a) ��������������û���漰���Ľ׶� b) �ܿ��⵽���һλ c)ʵ��������ֱ�ۣ��ǵ��ƹ�ʽ��ֱ�ӱ�
��������ݹ飬���ܸ����ϵ��ƹ�ʽ��
