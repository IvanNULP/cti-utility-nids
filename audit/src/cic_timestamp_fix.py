"""CIC-IDS2017: AM/PM timestamp correction and stratified temporal split (Sections 3.1 and 3.5).

The Timestamp field of the CICFlowMeter export uses a 12-hour clock without an AM/PM
designator. Capture ran from about 08:00 to 17:00, so every parsed hour below 8 is an
afternoon hour; adding 12 hours puts the DDoS, Infiltration and Heartbleed flows inside
the published attack windows.
"""
import numpy as np
import pandas as pd


def fix_ampm(ts: pd.Series, cutoff_hour: int = 8) -> pd.Series:
    """Return timestamps with +12 h added to every value whose hour is below `cutoff_hour`."""
    if not np.issubdtype(ts.dtype, np.datetime64):
        ts = pd.to_datetime(ts.astype(str), dayfirst=True, errors="coerce")
    return ts.where(ts.dt.hour >= cutoff_hour, ts + pd.Timedelta(hours=12))


def stratified_temporal_split(ts: pd.Series, label: pd.Series, q_train: float = 0.70, q_val: float = 0.85) -> pd.Series:
    """Apply the 70th/85th-percentile rule within each (capture day x class) group.

    Boundaries use quantile(..., interpolation="nearest"): train = t < b1, val = b1 <= t < b2,
    test = t >= b2. Temporal order is kept inside every group and every class reaches train and test.
    """
    grp = ts.dt.date.astype(str) + "|" + label.astype(str)
    tnum = ts.astype("int64")
    b1 = tnum.groupby(grp).transform(lambda s: s.quantile(q_train, interpolation="nearest"))
    b2 = tnum.groupby(grp).transform(lambda s: s.quantile(q_val, interpolation="nearest"))
    return pd.Series(np.where(tnum < b1, "train", np.where(tnum < b2, "val", "test")), index=ts.index)


def split_composition(label: pd.Series, split: pd.Series) -> pd.DataFrame:
    """Per-class flow counts by partition (Phase 0, step 2: split-composition audit)."""
    return pd.crosstab(label, split).reindex(columns=["train", "val", "test"], fill_value=0)
