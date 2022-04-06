from task_4.q1 import bounded_subset

if __name__ == "__main__":
    # -------------q1------------------
    for i in bounded_subset([1, 2, 3], 4):
        print(i)
    for i in bounded_subset([1,2,3,4,5,6,7,8,9],5):
        print(i)
    for i in bounded_subset([11,22,33,44,55,66,77,88,99], 50):
        print(i)
    for i in bounded_subset([100,100,100,100], 100):
        print(i)
    for i in bounded_subset([1,1,1,1,1,1],2):
        print(i)
    for i in bounded_subset([10,20,30,40,50],5):
        print(i)
