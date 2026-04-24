# Lambda functions is done in one line and has no return statement in them.

# Lambda function to check if a number is positive, negative, or zero

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))