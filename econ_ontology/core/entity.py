class Entity:
    def __init__(
        self,
        id: str,
        type: str,
        name: str = "",
        desc: str = "",
        category: str = "",
        source: str = "",
        unit: str = "",
        frequency: str = "",
        timezone: str = "",
        status: str = "active",
        # 금융/시장 관련
        currency: str = "",
        market: str = "",
        sector: str = "",
        region: str = "",
        ticker: str = "",
        asset_class: str = "",
        exchange: str = "",
        risk_level: str = "",
        volatility: float | None = None,
        # 거시경제 관련
        provider: str = "",
        definition: str = "",
        seasonal_adjustment: bool | None = None,
        lag: int | None = None,
        release_calendar: str = "",
        historical_range: str = "",
        # 이벤트 관련
        event_date: str = "",
        event_type: str = "",
        expected_value: float | None = None,
        actual_value: float | None = None,
        surprise: float | None = None,
        impact_level: str = "",
        # AI/LLM 관련
        embedding: list[float] | None = None,
        tags: list[str] | None = None,
        confidence_score: float | None = None,
        last_updated_by_ai: str = "",
        explanations: str = ""
    ):
        # 기본
        self.id = id
        self.type = type
        self.name = name
        self.desc = desc
        self.category = category
        self.source = source
        self.unit = unit
        self.frequency = frequency
        self.timezone = timezone
        self.status = status

        # 금융/시장
        self.currency = currency
        self.market = market
        self.sector = sector
        self.region = region
        self.ticker = ticker
        self.asset_class = asset_class
        self.exchange = exchange
        self.risk_level = risk_level
        self.volatility = volatility

        # 거시경제
        self.provider = provider
        self.definition = definition
        self.seasonal_adjustment = seasonal_adjustment
        self.lag = lag
        self.release_calendar = release_calendar
        self.historical_range = historical_range

        # 이벤트
        self.event_date = event_date
        self.event_type = event_type
        self.expected_value = expected_value
        self.actual_value = actual_value
        self.surprise = surprise
        self.impact_level = impact_level

        # AI/LLM
        self.embedding = embedding
        self.tags = tags or []
        self.confidence_score = confidence_score
        self.last_updated_by_ai = last_updated_by_ai
        self.explanations = explanations

    def __repr__(self):
        return f"Entity(id={self.id}, type={self.type}, name={self.name}, desc={self.desc})"
