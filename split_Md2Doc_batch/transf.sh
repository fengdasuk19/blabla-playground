ls > aa.md

cat aa.md |while read line
do
  pandoc $line -o $line.doc -c Github.css
done

rename 's/\.md.doc/\.doc/' *
rm *.md
