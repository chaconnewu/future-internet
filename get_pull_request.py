import requests
import json
import traceback
import csv
# r = requests.get('https://api.github.com/repos/EbookFoundation/free-programming-books/pulls\?sort\=created\&direction\=asc', auth=('chaconnewu', 'wuyu1985'))

# https://github.com/EbookFoundation/free-programming-books/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/tiimgreen/github-cheat-sheet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/papers-we-love/papers-we-love/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/kahun/awesome-sysadmin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/bayandin/awesome-awesomeness/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/vinta/awesome-python/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/bolshchikov/js-must-watch/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/cjbarber/ToolsOfTheTrade/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/avelino/awesome-go/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/zenorocha/alfred-workflows/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/sindresorhus/quick-look-plugins/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+
# https://github.com/justjavac/free-programming-books-zh_CN/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+created%3A%3C2014-09-01+

repo_base = 'https://api.github.com/repos/andreis/interview/'
res_file_name = 'interview.csv'
start = 1
# end = 959
end = 3

writer = csv.writer(open(res_file_name, 'w'))

for i in range(start, end+1):
    request_url = repo_base + 'pulls/' + str(i) + '/files'

    try:
        r = requests.get(request_url, auth=('chaconnewu', 'wuyu1985'))
        json_res = json.loads(r.text)

        add_cnt = 0
        del_cnt = 0
        for f in json_res:
            add_cnt += f['additions']
            del_cnt += f['deletions']

        print([i, add_cnt, del_cnt])
        writer.writerow([i, add_cnt, del_cnt])
    except:
        continue

del writer
res_file_name
