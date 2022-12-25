import re
cat='rongjanai'
for i in range(1,1458):
    f = open('sentinel/'+str(cat)+'/sentinel-'+str(re.sub('_','-',cat))+'-'+str(i)+'.txt', 'r', encoding='utf-8')
    n = 0
    news_text = ''
    for l in f:
        l = l.strip()
        n += 1
        if n==1:
            l = re.sub('TITLE:', '\n', l)
            l = l.strip()
            l = l +"\n"
        if re.search('Also Read',l):
            break
        if re.search('©',l):
            break
        if n>1 and n<6:
            continue
        else:
            l = re.sub('', ' ', l)  
            if len(l)<20:
                nl = '\b'
            else:
                nl = '\n'
            news_text = news_text + l + nl
            #print(l)
            
    w = open('sentinel-processed/'+str(cat)+'/sentinel-'+str(cat)+'-'+str(i)+'.txt', 'w', encoding='utf-8')
    w.write(news_text)
    w.close()
    f.close()