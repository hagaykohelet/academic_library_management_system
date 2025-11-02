class Logger:
    @staticmethod
    def log_action(action_type: str, details: str) -> None:
        print(f"the action: {action_type} details: {details}")

