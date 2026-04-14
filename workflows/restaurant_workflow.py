from agents.fetch_agent import DataFetchingAgent
from agents.process_agent import DataProcessingAgent
from agents.analytics_agent import RevenueAnalyticsAgent

class RestaurantWorkflow:

    def __init__(self):
        self.fetcher = DataFetchingAgent("Fetcher")
        self.processor = DataProcessingAgent("Processor", ["name", "type"])
        self.analytics = RevenueAnalyticsAgent("RevenueAgent")

    def run(self, restaurant_id):
        data = self.fetcher.execute(restaurant_id)

        if "error" in data:
            return data

        processed = self.processor.execute(data)
        revenue = self.analytics.execute(restaurant_id)

        return {
            "restaurant": processed,
            "analytics": revenue
        }
