"""Block bootstrap for differences in average precision (Section 4.9, Eq. 15)."""
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score


def minute_blocks(ts_test: pd.Series):
    """Indices of test flows grouped into 1-minute blocks."""
    blk = pd.factorize(ts_test.dt.floor("min"))[0]
    return list(pd.Series(np.arange(len(blk))).groupby(blk).indices.values())


def block_bootstrap_dap(y, p_a, p_b, blocks, n_boot=500, seed=42):
    """Point dAP = AP(a) - AP(b), 95% percentile CI and one-sided p = (1 + #{d_b <= 0}) / (1 + B)."""
    y, p_a, p_b = np.asarray(y), np.asarray(p_a), np.asarray(p_b)
    rng = np.random.default_rng(seed)
    point = average_precision_score(y, p_a) - average_precision_score(y, p_b)
    d = np.empty(n_boot)
    for b in range(n_boot):
        j = np.concatenate([blocks[k] for k in rng.integers(0, len(blocks), len(blocks))])
        d[b] = average_precision_score(y[j], p_a[j]) - average_precision_score(y[j], p_b[j])
    lo, hi = np.percentile(d, [2.5, 97.5])
    p = (1 + np.sum(d <= 0)) / (1 + n_boot)
    return {"dAP": point, "ci_lo": lo, "ci_hi": hi, "p_one_sided": p}


def holm(pvals):
    """Holm-adjusted p-values (same order as input)."""
    p = np.asarray(pvals, dtype=float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(p) - rank) * p[i])
        adj[i] = min(1.0, running)
    return adj
