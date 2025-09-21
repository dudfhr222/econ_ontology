from textwrap import dedent

def build_report(corr, scenario, es_cum) -> str:
    return dedent(f"""
    # 경제 온톨로지 리포트

    ## 상관관계 (corr)
    {corr.round(3).to_string()}

    ## 금리 시나리오별 S&P500 평균 반응 (%)
    {scenario.round(3).to_string()}

    ## 이벤트 스터디 (누적 평균 %)
    {es_cum.round(3).to_string()}
    """)
