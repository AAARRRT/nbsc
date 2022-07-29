from cn_nbs import load_nbs_web

x = load_nbs_web(series='A0201', periods="LAST5", freq='year')

print(x)


