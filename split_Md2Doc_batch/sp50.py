#coding: utf-8

originPath = "/home/sushangjun/Documents/"
srcPath = originPath + "Top50Bussiness.txt"
tarPath = originPath + "output50/"

fin = open(srcPath, 'r')

finContent = fin.read()

sp50 = finContent.split("\n##", 49)

for iStr in sp50:
    index = ((((iStr.split("\n\n![](")[0]).split('.'))[1]).split(' '))[1]
    fout = open(tarPath + "{}.md".format(index), 'w')
    fout.write("## " + index + "\n\n![](" + (iStr.split("\n\n![]("))[1])
    fout.close()

fin.close()
