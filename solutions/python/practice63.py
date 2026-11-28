# Problem: Bigger Price
# Source: https://py.checkio.org/en/mission/bigger-price/
# Note: Returns the most expensive products from a list of dictionaries.
# Description:
# Given a limit and a list of dictionaries with "name" and "price" keys, return the top "limit" items
# with the highest prices, sorted from highest to lowest. Items with equal prices retain their input order.
# 
# Example:
# - Input: limit=2, data=[{"name": "bread", "price": 100}, {"name": "wine", "price": 138}, ...]
# - Output: [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
# 
# Status: ✅ SOLVED

def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    if limit <= 0 or not data:
        return []

    return sorted(data, key=lambda item: item.get("price", 0), reverse=True)[:limit]
