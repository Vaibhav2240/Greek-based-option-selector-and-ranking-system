from __future__ import annotations

from typing import Any

import pandas as pd

from app.data.nse_client import NSEClient


class OptionChainService:
    """
    Converts NSE response into a clean dataframe.
    """

    def __init__(self, client: NSEClient | None = None) -> None:
        self.client = client or NSEClient()

    def fetch_option_chain(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        raw_data = self.client.get_option_chain(symbol)

        records: list[dict[str, Any]] = []

        for strike in raw_data["records"]["data"]:

            ce = strike.get("CE")
            pe = strike.get("PE")

            if not ce and not pe:
                continue

            records.append(
                {
                    "strike_price": strike.get("strikePrice"),

                    "ce_oi": ce.get("openInterest") if ce else None,
                    "ce_volume": ce.get("totalTradedVolume") if ce else None,
                    "ce_iv": ce.get("impliedVolatility") if ce else None,
                    "ce_ltp": ce.get("lastPrice") if ce else None,

                    "pe_oi": pe.get("openInterest") if pe else None,
                    "pe_volume": pe.get("totalTradedVolume") if pe else None,
                    "pe_iv": pe.get("impliedVolatility") if pe else None,
                    "pe_ltp": pe.get("lastPrice") if pe else None,
                }
            )

        return pd.DataFrame(records)