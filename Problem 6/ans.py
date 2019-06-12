ssq=sum([x**2 for x in range(1,101)])
sqs=(sum([x for x in range(1,101)]))**2
print("Difference between first hundred natural numbers: %d"%abs(ssq-sqs))