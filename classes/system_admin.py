# from classes.library import Library
class SystemAdmin:
    total_transactions = 0

    @classmethod

    def update_transactions_count(cls,amount:int = 1):
        cls.total_transactions += amount

    @classmethod

    def report_stats(cls,Library):
        print(f"total transactions is: {cls.total_transactions} days left to borrow {Library.max_borrow_days} ")



