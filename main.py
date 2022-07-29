from cn_nbs import load_nbs_web

x = load_nbs_web(series='A01030101', periods="LAST5", freq='month')

print(x)


