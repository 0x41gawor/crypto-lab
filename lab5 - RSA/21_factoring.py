import primefac

N = 510143758735509025530880200653196460532653147  
pnq = list(primefac.primefac(N, trial_limit=1000, rho_rounds=42000, verbose=True))
p = str(pnq[0]).strip('mqz(L)')
q = str(pnq[1]).strip('mqz(L)')
spacer = "-" * 64
print(f"P: {0}".format(p))
print(spacer)
print(f"Q: {0}".format(q))

# opis w readme



