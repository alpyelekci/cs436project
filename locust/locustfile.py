from locust import HttpUser, task, between

class FlaskyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_all_posts(self):
        self.client.get("/api/posts/")

    @task
    def create_post(self):
        self.client.post("/api/posts/", json={
            "body": "this is a test post from locust"
        })
