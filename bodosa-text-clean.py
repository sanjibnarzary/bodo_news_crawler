import re
for i in range(1,708):
    f = open('bodosa_news_crawled/bodosa-news-'+str(i)+'.txt', 'r', encoding='utf-8')
    n = 0
    news_text = ''
    for l in f:
        l = l.strip()
        n += 1
        if n==1:
            l = re.sub('- Bodosa Newspaper', '\n', l)
        if re.search('Related Posts',l):
            break
        if n>1 and n<5:
            continue
        else:
            if len(l)<20:
                nl = ''
            else:
                nl = '\n'
            news_text = news_text + l + nl
            
    w = open('bodosa_news_crawled_processed/bodosa-news-'+str(i)+'.txt', 'w', encoding='utf-8')
    w.write(news_text)
    w.close()
    f.close()