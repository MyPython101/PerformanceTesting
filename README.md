# Performance Testing Roles in Software Testing: Approach, Use Case, and Automated Performance Testing

**Abstract**  
This document introduces performance testing, discusses an approach to performance testing, and presents a case study
using LocustIO to perform automated performance testing on a blog website.

**Keywords**  
Software performance testing, performance testing, software testing.

---

## 1. Introduction

### a. Performance Testing Definition

Performance testing is a non-functional testing technique performed to evaluate the responsiveness, scalability, and
stability of a software system under various workloads. Key performance testing metrics include scalability,
reliability, and resource usage. There are four primary types of performance testing:

- **Load Testing**: Evaluates system behavior under expected user load.
- **Stress Testing**: Tests the system under extreme workloads to identify breaking points.
- **Soak Testing**: Checks system behavior over extended periods of sustained load.
- **Spike Testing**: Assesses how the system handles sudden spikes in user load.

### b. System Performance Degradation

According to [1], system performance degradation—such as failure to handle required throughput—poses significant
challenges for large industrial projects. While many systems undergo extensive functional testing, performance testing
is often neglected, resulting in critical performance issues during deployment.

AT&T engineers discovered during an architecture review that **performance issues** were among the top three major fault
categories. These issues included:

- Lack of performance estimates.
- Absence of data collection plans.
- Failure to allocate a performance budget.

Such inadequacies in planning can result in major user dissatisfaction upon deployment.

### c. Uneven Distribution of Resource Usage

A Pareto-type distribution—where 70% of the most severe problems reside in the weakest 30% of the system—can cause
significant performance degradation. Addressing this uneven distribution is critical for resolving project-impacting
issues.

---

## 2. Previous Work

As noted in [1], there is a scarcity of adequate resources on performance testing. The author observed a lack of
research literature or practical information to assist testers in carrying out effective software performance testing.

---

## 3. Performance Testing Tools

### a. LocustIO

Locust is a scriptable and scalable performance testing tool that is highly developer-friendly. It uses Python
programming for writing test scenarios, making it easy to integrate into developer workflows. Key features include:

- **Scriptable in Python**: Test scenarios can be written as Python code, with support for loops, conditions, and
  calculations.
- **Distributed & Scalable**: Locust supports load tests distributed across multiple machines, handling thousands of
  concurrent users in a single process.
- **Key Features**: Includes Docker support, distributed load generation, testing non-HTTP systems, CSV-based test
  results, and integration with Terraform/AWS.

### b. Expertus

According to [4], Expertus is designed to automate large-scale experiments in IaaS clouds, addressing challenges such as
performance scenario variation, efficient application startup in distributed environments, and cloud migration
complexities.

---

## 4. Use Case: Performance Testing a Blog Website Using LocustIO

### a. Application Overview

The application, **Blog-Template**, is a Flask-based blog with PostgreSQL for database management. It allows registered
users to edit or comment on posts, while only admins can create or delete posts. The blog was originally designed by Dr.
Angela Yu and implemented by Truc Huynh.

The app is hosted on Heroku, and its source code is available on [GitHub](https://github.com/jackyhuynh/blog-template).

### b. Backend Structure

The `main.py` file contains all the necessary components for running the app, including routes for the frontend (built
with HTML, CSS, and Bootstrap) and backend integration with PostgreSQL. Every change pushed to GitHub automatically
updates the live version on Heroku.

### c. Test Plan Design

The test plan involves simulating user behavior on the blog website, starting with 1,000 users at a spawn rate of 1 user
per second and gradually increasing to 3 million users. The test tasks include logging in, visiting the contact page,
and viewing post number 1.

### d. Test Suite Implementation

The performance test is implemented in Locust using Python. The script simulates user behavior with randomized wait
times to mimic real-world interaction patterns.

```python
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
```

### e. Test Results

Results from the initial test with 1,000 users at a spawn rate of 1 show a 0% failure rate. Locust provides real-time
monitoring through a web interface, and test data can be exported for further analysis.

---

## 5. Advantages and Disadvantages of Locust

### a. Advantages

- Verifies system speed, stability, and scalability.
- Open-source and free to use.
- Supports distributed testing with Python-based test cases.

### b. Disadvantages

- Requires Python programming knowledge.
- Inaccurate results if tests are not properly designed or executed.

---

## References

1. D. Jayasinghe et al., "Expertus: A Generator Approach to Automate Performance Testing in IaaS Clouds," *2012 IEEE
   Fifth International Conference on Cloud Computing*, pp. 115-122, doi: 10.1109/CLOUD.2012.98.
2. C. Bystron, J. Heyman, J. Hamren, H. Heyman, L. Holmberg, *LocustIO
   Documentation*, [GitHub](https://github.com/locustio/locust).