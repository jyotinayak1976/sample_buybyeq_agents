from agents.base_agent import Agent
from db.connection import Database

class RevenueAnalyticsAgent(Agent):
    def execute(self, restaurant_id):
        conn = Database.get_instance().get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT SUM(amount) FROM orders WHERE restaurant_id=?",
            (restaurant_id,)
        )

        revenue = cursor.fetchone()[0]

        return {"restaurant_id": restaurant_id, "total_revenue": revenue or 0}
