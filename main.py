from db.init_db import init_db
from workflows.restaurant_workflow import RestaurantWorkflow

if __name__ == "__main__":
    init_db()

    workflow = RestaurantWorkflow()

    print("\n--- RUN 1 ---")
    print(workflow.run("001"))

    print("\n--- RUN 2 ---")
    print(workflow.run("999"))
