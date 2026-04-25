def hit_rate(results, keyword):
    return any(keyword in r[1]["chunk"] for r in results)
