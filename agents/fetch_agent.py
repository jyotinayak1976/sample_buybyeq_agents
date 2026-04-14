from agents.base_agent import Agent
from db.connection import Database

class DataFetchingAgent(Agent):
    def execute(self, restaurant_id):
        conn = Database.get_instance().get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM restaurants WHERE restaurant_id=?", (restaurant_id,))
        row = cursor.fetchone()

        if not row:
            return {"error": "Restaurant not found"}

        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))
