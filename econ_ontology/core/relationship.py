class Relationship:
    def __init__(
        self,
        src: str,
        dst: str,
        rel: list[str] | str,
        weight: float | None = None,
        lag: int = 0,
        evidence: str = "",
        source: str = "",
        confidence: float | None = None,
    ):
        self.src = src
        self.dst = dst
        # 문자열 하나 들어와도 리스트로 변환
        self.rel = rel if isinstance(rel, list) else [rel]
        self.weight = weight
        self.lag = lag
        self.evidence = evidence
        self.source = source
        self.confidence = confidence

    def __repr__(self):
        return (
            f"Relationship(src={self.src}, dst={self.dst}, "
            f"rel={self.rel}, weight={self.weight}, lag={self.lag}, "
            f"confidence={self.confidence})"
        )

    def to_row(self) -> dict:
        """데이터프레임에 넣을 수 있게 dict 변환"""
        return {
            "src": self.src,
            "dst": self.dst,
            "rel": ",".join(self.rel),
            "weight": self.weight,
            "lag": self.lag,
            "evidence": self.evidence,
            "source": self.source,
            "confidence": self.confidence,
        }
