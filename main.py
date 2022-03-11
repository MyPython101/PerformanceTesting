from locust import HttpUser, task, between


class TestCases(HttpUser):
    host = "https://template-blog.herokuapp.com/"
    # Set the wait time for each user from 1 to 300 second
    # So that each user will be able to navigate and read 1 post or do some comment
    wait_time = between(1, 300)

    # When user in login the user
    def on_start(self):
        self.client.post("/login", json={"Email": "jackyhuynh87@gmail.com", "Password":"1234"})

    # task number 1 is to navigate to contact page (and stay there for 40 second)
    @task(10)
    def visit_contact(self):
        self.client.get("/contact")

    # after 50 second navigate to the post 1
    @task(50)
    def visit_post_1(self):
        self.client.get("/post/1")
