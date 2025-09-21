# AI 해석 (자연어 evidence 생성)
from econ_ontology.analysis.ai.ollama_client import ollama_chat

def generate_evidence(src: str, dst: str, rel: list[str], weight: float | None, lag: int) -> str:
    """
    Ollama LLM을 이용해 관계 설명을 자연어로 생성
    """
    user_text = (
        f"{src} 와 {dst} 의 관계는 {','.join(rel)} 입니다. "
        f"상관계수는 {weight} (자동 계산됨), "
        f"시차(lag)는 {lag} 일입니다. "
        f"이를 한국어로 간단히 설명해줘."
    )

    system_msg = {"role": "system", "content": "너는 경제/금융 분석 전문가다. 짧게 요약하라."}
    user_msg = {"role": "user", "content": user_text}

    try:
        return ollama_chat([system_msg, user_msg])
    except Exception as e:
        return f"(evidence 생성 실패: {e})"
