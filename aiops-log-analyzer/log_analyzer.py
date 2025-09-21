import pandas as pd
import numpy as np

def detect_spikes(df, window=5, z=3.0):
    roll = df['errors'].rolling(window).mean()
    std = df['errors'].rolling(window).std().replace(0, np.nan)
    zscores = (df['errors'] - roll) / std
    df['anomaly'] = zscores.abs() > z
    return df

if __name__ == "__main__":
    # demo data
    ts = pd.date_range("2025-01-01", periods=60, freq="T")
    errors = np.random.poisson(lam=1, size=60)
    errors[30:33] += 10  # inject anomaly
    df = pd.DataFrame({"ts": ts, "errors": errors}).set_index("ts")
    out = detect_spikes(df.copy())
    print(out.tail(10))