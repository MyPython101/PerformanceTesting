# Performance Testing

**Abstract** - An Introduction to Performance Testing. An approach to performance testing is discussed. A case study using 
locustio to perform performance testing on a blog website is presented

**Index Terms** - Software performance testing, performance testing, software testing.

## 1. Introduction

### a. Performance Testing Definition

Performance testing is a testing technique, performed to determine the responsiveness and stability of 
a software system under various workload.
Performance testing metrics are scalability, reliability, resource usage. 
There are four primary type of performance testing: Load Testing, Stress Testing, Soak Testing, and Spike Testing. 
Performance testing is a non-functional testing [3].

### b. System Performance Degradation

According to [1], system performance degradation or problems handling required system
throughput is an extremely significant issue for many large industrial projects. Although the software system has gone through
extensive functionality testing, it was never really tested to assess its expected performance [1].

During an architecture review at AT&T, a group of engineer have found that "performance issues
account for one of the three major fault categories. Performance problems identified might include
such things as the lack of performance estimates, the failure to have proposed plans for data collection, 
or the lack of a performance budget". They also claimed that insufficient planning for performance issues
is the major issues when the software deploy to the field [1].

Major issues are issues that will impact on user satisfaction.

### c. Uneven Distribution of Resource Usage

Pareto-type distribution is also known as very uneven distribution of resource usage. The main reason for system performance degradation
is claimed distribution of project-affecting issues (Pareto-type distribution). According to [1], it was found that 70 percent of the most severe class of problems 
resided in the weakest 30 percent of the project.

## Previous Work:

According to [1], The author doesn't find an adequate of performance testing knowledge on the Internet. He found out that "there is neither an
existing body of research literature nor an extensive collection of practical or experiential information available
to help testers faced with the prospect of doing software performance testing".


## Locust IO
### Introduction:

Locust is a scriptable and scalable performance testing tool, 





```bash
2022-03-10T17:00:41Z
[2022-03-10 12:00:41,483] DESKTOP-J4K30PB/INFO/locust.main: Shutting down (exit code 1)
 Name                                                                              # reqs      # fails  |     Avg     Min     Max  Median  |   req/s failures/s
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 GET //contact                                                                       1095     1(0.09%)  |     120      27   19214     130  |    0.81    0.00
 POST //login                                                                        1000     0(0.00%)  |     144     114    1134     140  |    0.74    0.00
 GET //post/1                                                                        5162     4(0.08%)  |     125      28   25672     140  |    3.83    0.00
----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 2                  GET //post/1: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)
 2                  GET //post/1: RemoteDisconnected('Remote end closed connection without response')
 1                  GET //contact: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 Name                                                                              # reqs      # fails  |     Avg     Min     Max  Median  |   req/s failures/s
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 GET //contact                                                                          1     0(0.00%)  |      42      42      42      42  |    0.01    0.00
 POST //login                                                                          10     0(0.00%)  |     162     137     181     160  |    0.05    0.00
 GET //post/1                                                                          18     0(0.00%)  |     106      40     194      66  |    0.09    0.00
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 Aggregated                                                                            29     0(0.00%)  |     123      40     194     150  |    0.15    0.00

Response time percentiles (approximated)
 Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 GET      //contact                                                                              42     42     42     42     42     42     42     42     42     42     42      1
 POST     //login                                                                               170    170    170    170    180    180    180    180    180    180    180     10
 GET      //post/1                                                                               69    170    170    170    180    190    190    190    190    190    190     18
--------|--------------------------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 None     Aggregated                                                                            150    170    170    170    180    180    190    190    190    190    190     29

```

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
 
