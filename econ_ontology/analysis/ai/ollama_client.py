import requests, json
from econ_ontology.config.settings import settings

def ollama_chat(messages: list[dict], model: str | None = None, stream: bool = False) -> str:
    url = f"{settings.OLLAMA_ENDPOINT}/api/chat"
    payload = {"model": model or settings.OLLAMA_MODEL, "messages": messages, "stream": stream}
    r = requests.post(url, json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    return data.get("message", {}).get("content", "")

def turn_nl_to_json(nl: str) -> dict:
    """자연어 관계 설명을 JSON 스펙으로 변환"""
    system = {
        "role": "system",
        "content": "자연어 관계 설명을 JSON으로만 출력해. "
                   "예시: {\"src\":\"BTC_USD\",\"dst\":\"NASDAQ_Index\",\"rel\":[\"correlated_with\"],\"weight\":\"auto\",\"lag\":\"auto\"}"
    }
    user = {"role":"user","content": nl}
    text = ollama_chat([system, user])
    try:
        return json.loads(text)
    except Exception:
        return {
            "src": "",
            "dst": "",
            "rel": ["related_to"],
            "weight": "auto",
            "lag": "auto",
            "notes": nl
        }
