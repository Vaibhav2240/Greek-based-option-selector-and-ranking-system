from __future__ import annotations

import requests

from app.config.settings import config


class NSEClient:
    """
    Responsible only for communicating with NSE.
    """

    def __init__(self) -> None:
        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept": "application/json",
                "Referer": config.nse_base_url,
            }
        )

    def initialize_session(self) -> None:
        """
        NSE often requires a preliminary request
        to establish cookies.
        """

        self.session.get(
            config.nse_base_url,
            timeout=config.request_timeout,
        )

    def get_option_chain(self, symbol: str) -> dict:
        """
        Fetch raw option chain JSON.
        """

        self.initialize_session()

        response = self.session.get(
            f"{config.option_chain_endpoint}?symbol={symbol}",
            timeout=config.request_timeout,
        )

        response.raise_for_status()

        return response.json()