# --------------this is the code to re take input form the user if the code is't in the "integer format"--------------------------------
j, jj, m = [], [], [[], [], []]

def fd(th_u6, f_4hg, nu_t3):  # function for taking input from user
    condense = range(0, 9)  # this var is use to re take input 9 times if user enter wrong input
    for _ in condense:  # for loop is for  retake input from user in the range 9 if the input is !in the form of integer
        try:  # this is to retake input from user if the entered value is!int it jump to the except statment
            print("Enter the value of", f_4hg, ":")  # f_4hg print for which positioon you are entring value
            j_gq5 = int(input())  # this line will genrate ereer if the valu is not in the integer form
            th_u6[nu_t3].append(j_gq5)  # this statment will work only if there is not any error in the abbove statment
            break  # this break function will break the for loop of there is not any error occure in try segment
        except:  # function jump to this except statment if error occure on the line 9
            print("you  entered  wrong value Dummy you can't add float or string :")  # the for loop will continue
            
 x11, x12, x13 = fd(m, 'x11', 0), fd(m, 'x12', 0), fd(m, 'x13', 0)
# x21, x22, x23 = fd(m, 'x21', 1), fd(m, 'x22', 1), fd(m, 'x33', 2)
# x31, x32, x33 = fd(m, 'x23', 1), fd(m, 'x31', 2), fd(m, 'x32', 2)
