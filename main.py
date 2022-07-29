from cn_nbs import load_nbs_web

"""

http://data.stats.gov.cn/english/easyquery.htm?m=QueryData
&dbcode=hgyd
&rowcode=zb
&colcode=sj
&wds=[]
&dfwds=[{"wdcode":"sj","valuecode":"LATEST1"},{"wdcode":"zb","valuecode":"A01030101"}]
&k1=1659089890739
&h=1
"""

x = load_nbs_web(series='A01030101', periods="LAST5", freq='month')

print(x)


