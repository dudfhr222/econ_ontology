# 결과 요약

def summarize_results(results: dict) -> str:
    """분석 결과를 텍스트 요약"""
    lines = []
    for k, v in results.items():
        lines.append(f"{k}: {v}")
    return "\n".join(lines)
