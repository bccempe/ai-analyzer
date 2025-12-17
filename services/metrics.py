class MetricsService:
    def __init__(self):
        self.repository = AppRepository()

    def get_metrics(self, app_id: str) -> list[Metric]:
        return self.repository.get_metrics(app_id)