import pandas as pd


def summarize_top_drivers(feature_importance: pd.DataFrame, top_n: int = 8) -> pd.DataFrame:
    return (
        feature_importance.sort_values("importance", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )

