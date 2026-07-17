try:
    a = int(input("Hey! Enter the number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I'm inside Finally")    # This executed regradless of error!



# If finally run regardless of try was successful or not. Then won't be the
#
# finally:
#     print("I'm inside else")
#
#         AND
#
#  print("I'm inside else")
#
# same.
#
# """Yeah! It is same. But finally's main use is in function."""
#
# Look the follwing piece of code 👇



def main():
    try:
        a = int(input("Hey! Enter the number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I'm inside Finally")

main()


# If it was only
# 
# print("I'm inside Finally")
# 
# then it won't be executed as both try and except block exit the function block after execution beacuse of return.
# 
# but if we use """finally""" it executed regardless