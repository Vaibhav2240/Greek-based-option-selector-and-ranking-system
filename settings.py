from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """
    Central application configuration.
    """

    app_name: str = "NIFTY Options Analytics"
    default_index: str = "NIFTY"
    request_timeout: int = 10


config = AppConfig()