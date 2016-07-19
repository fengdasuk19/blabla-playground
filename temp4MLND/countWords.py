#coding: utf-8
"""Count words."""
"""
用 Python 统计字数
问题
用 Python 实现函数 count_words()，
该函数输入字符串 s 和数字 n，
返回 s 中 n 个出现频率最高的单词。
    返回值是一个元组列表，包含出现次数最高的 n 个单词及其次数,即 [(<单词1>, <次数1>), (<单词2>, <次数2>), ... ]，按出现次数降序排列。

您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个空格）。
如果出现次数相同，则按字母顺序排列。

例如：

print count_words("betty bought a bit of butter but the butter was bitter",3)
输出：

[('butter', 2), ('a', 1), ('betty', 1)]
说明
这是一个 Python 的编程练习。下个页面会出现一个简单的代码编辑器。按照模版代码的指示完成这个练习（在"TODO"位置写下你的代码）。

你可以按 Test Run（测试运行）按钮来运行你的程序。输出会在编辑器下方显示。

要检查您的答案是否正确，请使用 Submit（提交） 按钮，并在右侧查看反馈信息。您可根据自身需要反复查看。
"""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # Preparation    
    wordsCounting = {}
    resultRaw = []
    top_n = []
    # TODO: Count the number of occurences of each word in s
    wordsRaw = s.split(' ')
    for w in wordsRaw:
        if w in wordsCounting.keys():
            wordsCounting[w] += 1
        else:
            wordsCounting[w] = 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    for eachKey in  wordsCounting.keys():
        resultRaw.append((eachKey, wordsCounting[eachKey]))

    tempList = []
    lastMax = max(resultRaw, key=lambda value:value[1])
    for i in range(len(wordsCounting)):
        tempMax = max(resultRaw, key=lambda value:value[1])
        if (tempMax[1] != lastMax[1]):
            tempList = sorted(tempList, key=lambda value:value[0])
            top_n.extend(tempList)
            tempList = []
        tempList.append(tempMax)
        lastMax = tempMax
        resultRaw.remove(tempMax)

    tempList = sorted(tempList, key=lambda value:value[0])
    top_n.extend(tempList)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

