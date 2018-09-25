import difflib
# import os
# with open('fhmg_out.csv', 'rb') as f:
#     a = f.readlines()
#     # print f1_text
# with open('fhmg_original.csv', 'rb') as f:
#     b = f.readlines()
#     # print f2_text
# # # # Find and print the diff:
# # for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
# #     print line
# print os.linesep.join(difflib.unified_diff(a,b))

import difflib

with open('fhmg_out.csv') as text1, open('fhmg_original.csv') as text2:
    diff = difflib.ndiff(text1.readlines(), text2.readlines())
with open('diff.txt', 'w') as result:
    for line in diff:
        result.write(line)
