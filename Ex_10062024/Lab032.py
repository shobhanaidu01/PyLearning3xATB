# Ternary Operator
pramod_marks = 90
amit_marks = 97

#   x > y -> do something - print("pramod")
# y > x -> do something else -> print("amit)
print("pramod is winner" if pramod_marks > amit_marks else "amit is winner")


if pramod_marks > amit_marks:
    print("pramod is the winner")
else:
    print("Amit is the winner")


Shobha_age = 28
Naidu_age = 29

if Shobha_age < Naidu_age:
    print("Shobha is younger")
else:
    print("Naidu is younger")

print("Shobha is younger" if Shobha_age < Naidu_age else "Naidu is younger")