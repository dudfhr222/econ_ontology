from econ_ontology.analysis.ai.correlation import compute_relationship_weight
from econ_ontology.core.relationship import Relationship

def update_relationship_weight(ts, relationship: Relationship) -> Relationship:
    """시계열 데이터 기반으로 관계 객체의 weight 업데이트"""
    weight = compute_relationship_weight(ts, relationship.src, relationship.dst)
    if weight is not None:
        relationship.weight = round(weight, 3)
        relationship.evidence = (
            f"Auto-computed correlation from {relationship.src} and {relationship.dst} time series"
        )
        relationship.confidence = 0.95  # 분석기준 신뢰도 부여
    return relationship
