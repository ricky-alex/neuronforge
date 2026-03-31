def safe_get(data: dict, key: str, default=None):
    return data.get(key, default)

def chunk_list(lst: list, size: int) -> list:
    return [lst[i:i + size] for i in range(0, len(lst), size)]
