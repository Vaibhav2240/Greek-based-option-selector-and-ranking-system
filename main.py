from app.config.settings import config


def main() -> None:
    print(f"Starting {config.app_name}")


if __name__ == "__main__":
    main()