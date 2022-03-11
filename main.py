from locust import HttpUser, task, between


class TestCases(HttpUser):
    host = "https://template-blog.herokuapp.com/"
    wait_time = between(1, 300)

    def on_start(self):
        self.client.post("/login", json={"Email": "jackyhuynh87@gmail.com", "Password":"1234"})

    @task(10)
    def visit_contact(self):
        self.client.get("/contact")

    @task(50)
    def visit_post_1(self):
        self.client.get("/post/1")
