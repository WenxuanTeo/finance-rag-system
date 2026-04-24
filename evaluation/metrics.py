def hit_rate(results, target_keyword):
    hit = 0
    for score, item in results:
        if target_keyword in item["chunk"]:
            hit += 1
    return hit / len(results)
