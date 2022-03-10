# Performance Testing

**Abstract** - An Introduction to Performance Testing. An approach to performance testing is discussed. A case study using 
locustio to perform performance testing on a blog website is presented

**Index Terms** - Software performance testing, performance testing, software testing.

## 1. Introduction:
### a. Performance Testing Definition 
Performance testing is a testing technique, performed to determine the responsiveness and stability of 
a software system under various workload.
Performance testing metrics are scalability, reliability, resource usage. 
There are four primary type of performance testing: Load Testing, Stress Testing, Soak Testing, and Spike Testing. 
Performance testing is a non-functional testing [3].

### b. System Performance Degradation:
According to [1], system performance degradation or problems handling required system
throughput is an extremely significant issue for many large industrial projects. Although the software system has gone through
extensive functionality testing, it was never really tested to assess its expected performance [1].

During an architecture review at AT&T, a group of engineer have found that "performance issues
account for one of the three major fault categories. Performance problems identified might include
such things as the lack of performance estimates, the failure to have proposed plans for data collection, 
or the lack of a performance budget". They also claimed that insufficient planning for performance issues
is the major issues when the software deploy to the field [1].

Major issues are issues that will impact on user satisfaction.

### c. Uneven distribution of resource usage
Pareto-type distribution is also known as very uneven distribution of resource usage.

## B. Example/Explain:
### Example 1 using Locustio
- we can perform performance testing using Python 
- locust package of Python can perform this task.
- locust is coding base package. Therefore, we can store as script and perform this with other testing technique
- install from bash

```bash
$ pip install locustio
```
- Boiler of performance testing script may look like:
```python
from locust import HttpLocust, TaskSet, task, between

class TestCases(TaskSet):
    def on_start(self):
        self.payload = {"email": "john@example.com", "password":123}
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("/login", self.payload)

    def logout(self):
        self.client.post("/logout", self.payload)

    @task(2)
    def visit_count(self):
        self.client.get("/visit")

    @task(1)
    def profile(self):
        self.client.get("/profile")

class LocustUsers(HttpLocust):
    task_set = TestCases
    wait_time = between(5, 9)
```
- Run the script above from bash
```bash
locust -f mylocustfile.py -- host= https://template-blog.herokuapp.com/
```
- If the code has no issue then we will see something like this
```bash
[2022-02-10 10:13:16,324]                     /INFO/locust.main: Starting web monitor at http://*:8089
```
- Navigate to local host http://localhost:8089, there is will be a graphic interface appear
```diff
- Enter the number of total user to simulate: 10000
- Enter the Hatch Rate: 99
+ If you give the number of users to simulate as 10000 and Hatch rate as 99 then all 10000 users will be activated within 99 seconds 
```
### Example 2 (using datetime package):
- There are methods that using datatime, timeit, cProfile for performance testing, but I may argue that it won't be efficient as the locustio package.
- May end up to manually do extra work compare to locustio

## C. Advantages/Disadvantage
### Advantage:
- Verifies the speed, accuracy, and stability of the software match expectation.
- Assists the system by authenticating the responsiveness and managing the scalability and reliability of software features.
- Retrieved from (14)

### Disadvantage:
- Can be a costly mistake if done haphazardly, leading to inaccurate results and conclusions.
- Carried out on multiple devices in different locations to check whether a user faces difficulties. Hence, this testing can be costly.
- Retrieved from (14)

## D. Applications:
- Performance testing should be performed for any kind of applications since we all want to know how our application is performed. 
We can guarantee the software applications can handle and manage the workload efficiently

## E. Reference:

E. J. Weyuker and F. I. Vokolos, "Experience with performance testing of software systems: issues, an approach, and case study," in IEEE Transactions on Software Engineering, vol. 26, no. 12, pp. 1147-1156, Dec. 2000, doi: 10.1109/32.888628. [1]

Kumar., K. Write your first performance/load test in Python., Retrieved from https://medium.com/@kundan3034/write-your-first-performance-load-test-in-python-e8e2132ef775 [2]

Tutorial Points (n.d.), "Performance Testing", Retrieved from https://www.tutorialspoint.com/software_testing_dictionary/performance_testing.htm [3]
 
