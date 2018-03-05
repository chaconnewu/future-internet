# if first == second == 0, skip

import os
import glob
import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

path = './'
extension = 'csv'
os.chdir(path)
files = [i for i in glob.glob('*.{}'.format(extension))]

here_cnt = 0
add_x = []
delete_x = []
update_x = []

for f in files:
    reader = csv.reader(open(f, 'r'))
    res = []
    add_cnt = 0
    delete_cnt = 0
    update_cnt = 0
    for line in reader:
        pr_num, addition, deletion = map(int, line)
        if addition == 0 and deletion == 0:
            continue

        if addition > 0 and deletion == 0:
            add_cnt += 1
            continue

        if addition == 0 and deletion > 0:
            delete_cnt += 1
            continue

        if addition > 0 and deletion > 0 and (addition - deletion) > deletion:
            add_cnt += 1
            continue

        if addition > 0 and deletion > 0 and (deletion - addition) > addition:
            delete_cnt += 1
            continue

        # if max(addition, deletion) <= 10 and abs(addition - deletion) <= 3:
        #     update_cnt += 1
        #     continue
        #
        # if min(addition, deletion) >= 10 and abs(addition - deletion) <= 5:
        #     update_cnt += 1
        #     continue


        # print(addition, deletion)
        update_cnt += 1

    total_cnt = add_cnt + delete_cnt + update_cnt
    # print("%s, %.2f, %.2f, %.2f" % (f, add_cnt / total_cnt, delete_cnt / total_cnt, update_cnt / total_cnt))
    add_per = add_cnt / total_cnt * 100
    delete_per = delete_cnt / total_cnt * 100
    update_per = update_cnt / total_cnt * 100

    # add_per = add_cnt / total_cnt
    # delete_per = delete_cnt / total_cnt
    # update_per = update_cnt / total_cnt

    add_x.append(add_per)
    delete_x.append(delete_per)
    update_x.append(update_per)

plt.rcParams["font.family"] = "Palatino Linotype"
plt.rcParams["font.size"] = 12
plt.figure()
fig, ax = plt.subplots()

labels = ['add', 'delete', 'update']
# print([add_x,delete_x,update_x])
ax.hist([add_x,delete_x,update_x], stacked=True,  color=[(0.45, 0.58, 0.80), (0.88,0.59,0.30), (0.83,0.37,0.38)], label=labels)
ax.legend()
ax.set_title("The repository counts vs. \nthe percentage of add, delete, and update related pull requests")
ax.set_xlabel('Percentage')
ax.set_ylabel('Repository Count')
x_ticks = [x/5 for x in range(10)]

ax.set_xticklabels(x_ticks)
# plt.show()
plt.savefig('repo_vs_pr.png')
