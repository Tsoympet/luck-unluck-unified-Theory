import argparse, numpy as np, pandas as pd

def wald_iv(L, A, Z):
    num = L[Z==1].mean() - L[Z==0].mean()
    den = A[Z==1].mean() - A[Z==0].mean()
    return num / den

def bootstrap_se(L, A, Z, B=5000, seed=123):
    rng = np.random.default_rng(seed)
    n = len(L); vals = []
    idx = np.arange(n)
    for _ in range(B):
        b = rng.choice(idx, size=n, replace=True)
        vals.append(wald_iv(L[b], A[b], Z[b]))
    return np.std(vals, ddof=1), np.quantile(vals, [0.025, 0.975])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="CSV with columns: L,A,Z (0/1)")
    ap.add_argument("--B", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=123)
    args = ap.parse_args()
    df = pd.read_csv(args.csv)
    L = df["L"].to_numpy()
    A = df["A"].to_numpy().astype(int)
    Z = df["Z"].to_numpy().astype(int)
    w = wald_iv(L,A,Z)
    se, ci = bootstrap_se(L,A,Z,B=args.B,seed=args.seed)
    print(f"Wald IV: {w:.4f}  SE_boot: {se:.4f}  95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]  (B={args.B}, seed={args.seed})")

if __name__ == "__main__":
    main()
