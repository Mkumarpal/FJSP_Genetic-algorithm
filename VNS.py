import random
import itertools as it
# from main_ga_code_final_20_01_22 import genetic_algorithm
# from bidding import manoj_code
from manoj_code_fjspwith_idleonly import manoj_code


# def insertion(best_child,critical_position,k=1):
#     randgroup_list=[]
# #     print("best_child1",best_child)
# #     print(len(best_child))
#     if isinstance(best_child[0], int):
#         new_best_child_1 = best_child
#     else:
#         if isinstance(best_child[0],str):
#             if len(best_child) == 1:
#                 y = str(best_child[0])
#                 new_best_child_1 = best_child.split()
#             else:
#                 y = best_child
#                 new_best_child_1 = best_child.split()
#         else:
#             new_best_child_1 = [eval(x) for x in best_child]
# #     print("best_child intital",new_best_child_1)
#     new_best_child = new_best_child_1.copy()
# #     print("critical postion",critical_position)
#     j = 0
#     while j<k:
#         randgroup = []
#         x = int(random.choice(critical_position))
# #         print("x",x)
#         randgroup.append(x)
#         while True:
#             y = random.randint(1,len(new_best_child)-1)
# #             print("y ki value", y)
# #             print("randgroup",randgroup)
#             if str(y) not in critical_position:
#                 randgroup.append(y)
#                 if randgroup not in randgroup_list:
#                     randgroup
#                 else:
# #                     print("randgroup", randgroup)
#                     randgroup.append(y)
#                     break
# #         print("randgroup",randgroup)
#         breakpoint()
#         randgroup_list.append(randgroup)
#         ch = new_best_child[randgroup[0]]
#         new_best_child.pop(randgroup[0])
#         new_best_child.insert(randgroup[1], ch)
# #         print(new_best_child)
#         j = j+1
#     return new_best_child

def swap(best_child2,critical_position, k=1):
    # print(k)
    randgroup_list=[]
    # print("best_child2",best_child2)
    if isinstance(best_child2[0], int):
        new_best_child_2 = best_child2
    else:
        if isinstance(best_child2[0],str):
            if len(best_child2)==1:
                y = str(best_child2[0])
                new_best_child_2 = best_child2.split()
            else:
                y = best_child2
                new_best_child_2 = best_child2.split()
        else:
            new_best_child_2 = [eval(x) for x in best_child2]
    # print("best_child2 initial",new_best_child_2)
    new_best_child2= new_best_child_2.copy()
    j = 0
    while j<k:
        randgroup = []
        # print(critical_position)
        x = int(random.choice(critical_position))
        # print("x", x)
        randgroup.append(x)
        while True:
            y = random.randint(2, len(new_best_child2) - 1)
            # print("y ki value", y)
            # print("randgroup", randgroup)
            if new_best_child2[x] != new_best_child2[y] or str(y) not in critical_position:
                randgroup.append(y)
                # print("random group", randgroup)
                if randgroup not in randgroup_list:
                    break
                else:
                    randgroup.remove(y)
                    # print("randomgroup",randgroup)
                    continue
            else:
                # print("randomgroup",randgroup)
                continue
        # print("randgroup",randgroup)
        randgroup_list.append(randgroup)
        # print("randgroup list",randgroup_list)
        ch = new_best_child2[randgroup[0]]
        # print("ch", ch)
        ch1 = new_best_child2[randgroup[1]]
        # print("ch1", ch1)
        # print(randgroup[0])
        # print(randgroup[1])
        new_best_child2.pop(randgroup[0])
        new_best_child2.insert(randgroup[0], ch1)
        new_best_child2.pop(randgroup[1])
        new_best_child2.insert(randgroup[1], ch)
        # print(new_best_child2)
        j = j+1
        # print (j)
    return new_best_child2

def reverse(best_child3,critical_position,k=1):
    randgroup_list=[]
    # print("best_child3", best_child3)
    new_best_child_3 = []
    if isinstance(best_child3[0], int):
        new_best_child_3 = best_child3
    else:
        if isinstance(best_child3, str):
            if len(best_child3) == 1:
                y = str(best_child3[0])
                new_best_child_3 = best_child3.split()
            else:
                y = best_child3
                new_best_child_3 = best_child3.split()
        else:
            new_best_child_3 = [eval(x) for x in best_child3]
    # print("best_child3 intital", new_best_child_3)
    new_best_child3 = new_best_child_3.copy()
    m = 0
    while m<k:
        randgroup = []
        # print("critical position",critical_position)
        x = int(random.choice(critical_position))
        # print("x", x)
        randgroup.append(x)
        while True:
            y = random.randint(2, len(new_best_child3) - 1)
            # print("y ki value", y)
            # print("randgroup", randgroup)
            if str(y) not in critical_position:
                randgroup.append(y)
                if randgroup not in randgroup_list:
                    break
                else:
                    randgroup.remove(y)
                    continue
            else:
                # print("randgroup", randgroup)
                continue
        # print("randgroup", randgroup)
        randgroup1 = randgroup.copy()
        randgroup.sort(reverse=True)
        randgroup_list.append(randgroup)
        # print("randgroup_list",randgroup_list)
        randgroup1.sort()
        # print(randgroup1)
        # print(randgroup)
        if randgroup[1]==0:
            newchild = new_best_child3[randgroup[0]::-1]
            # print("newchild",newchild)
        else:
            newchild = new_best_child3[randgroup[0]:randgroup[1]-1:-1]
        # print("newchild", newchild)
        j = 0
        for i in range(randgroup1[0] ,randgroup1[1]+1):
            new_best_child3.pop(i)
            new_best_child3.insert(i,newchild[j])
            j = j+1
        # print("bestchild3",new_best_child3)
        m = m+1
    return new_best_child3

#CHANGING THE NEIGHBOURHOOD OF A SPECIFIC SOLUTION:

def change_neighbourhood(initial_sol,no_jobs,no_of_machine):
    lmax = 3
    l = 0
    G_shake=[1,3,5]
    original_sol = initial_sol.copy()
    fitness_initial_sol = manoj_code(original_sol, no_jobs, no_of_machine)
    # print("fitness_initial_sol",fitness_initial_sol)
    fitness_initial_sol_value_list = list(fitness_initial_sol.values())
    fitness_initial_sol_value = fitness_initial_sol_value_list[0]
    # print("fitness_initial_sol_value",fitness_initial_sol_value)
    while l<lmax:
        # print("loop starts again")
        for i in G_shake:
            # print("original sol",original_sol)
            new_neighbour_sol=swap(original_sol,i)
            # print("new_neighbour_sol",new_neighbour_sol)
            fitness_new_neighbour_sol = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
            # print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
            fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
            fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
            # print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
            # print("fitness initial sol vlaue", fitness_initial_sol_value)
            if fitness_new_neighbour_sol_value < fitness_initial_sol_value:
                # print("yes yha change hua hai")
                original_sol= new_neighbour_sol
                fitness_initial_sol_value  = fitness_new_neighbour_sol_value
                l = 0
                break
            else:
                l = l+1
    #             print("l",l)
    #             print("orginal sol",original_sol)
    # print("original sol",original_sol)
    # print("l",l)
    # print("********************************************************************************************************************")
    return original_sol, fitness_initial_sol_value

# LOCAL SEARCH ALGO:
##########################
def local_search(starting_solution,no_jobs,no_of_machine):
    global new_solution_list
    global fitness_local_initial_sol_value
    initial_sol = starting_solution.copy()
    # current_critical_position = critical_position.copy()
    # print("current_critical_position",current_critical_position)
    G_Local=[[1,2,3,4],[2,4,6,8],[3,5,7,9],[4,6,8,10]]
    q = 0
    qmax = 3
    var = len(initial_sol)
    # print("variable",var)
    a = 0
    if var<=50:
        a = 0
    elif var<=100:
        a = 1
    elif var<=150:
        a = 2
    elif var>150:
        a = 3
    no_of_machine = no_of_machine
    no_jobs = no_jobs
    # print("initial-sol", initial_sol)
    local_initial_sol = initial_sol
    fitness_local_initial_sol,dict_of_position = manoj_code(local_initial_sol, no_jobs,no_of_machine)
    # print("fitness_initial_sol", fitness_local_initial_sol)
    # print("dict of postion",dict_of_position)
    fitness_local_initial_sol_value_list = list(fitness_local_initial_sol.values())
    fitness_local_initial_sol_value = fitness_local_initial_sol_value_list[0]
    # print("fitness local initial sol value",fitness_local_initial_sol_value)
    list_of_list_of_critical_position = list(dict_of_position.values())
    current_critical_position = list_of_list_of_critical_position[0]
    final_dict_of_position = {}
    while q < qmax:
        if q == 0:
            # print("q ki value",q)
            # print("local initial sol", local_initial_sol)
            j = G_Local[a][0]
            new_neighbour_sol = swap(local_initial_sol,current_critical_position,j)
            # print("local initial sol", local_initial_sol)
            # print("new neighbour sol", new_neighbour_sol)
            fitness_new_neighbour_sol,dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
            # print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
            # print("dict of position", dict_of_position)
            fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
            fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
            # print("fitness_new ngiehgbour sol value",fitness_new_neighbour_sol_value)
            # print("fitness local_initial_sol vlaue",fitness_local_initial_sol_value)
            if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
                # print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
                # print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
                # print("yes yha change hua hai")
                local_initial_sol = new_neighbour_sol
                fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
                list_of_list_of_critical_position = list(dict_of_position.values())
                current_critical_position = list_of_list_of_critical_position[0]
                # print("current critical postion ",current_critical_position)
                # print("local_initial_sol", local_initial_sol)
                q = 0
            else:
                q = q + 1
                # print("local initial sol", local_initial_sol)
        elif q == 1:
            # print("q ki value", q)
            j = G_Local[a][1]
            new_neighbour_sol = swap(local_initial_sol, current_critical_position, j)
            # print("local initial sol",local_initial_sol)
            # print("new neighbour sol",new_neighbour_sol)
            fitness_new_neighbour_sol,dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
            # print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
            fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
            fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
            # print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
            # print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
            if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
                # print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
                # print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
                # print("yes yha change hua hai")
                local_initial_sol = new_neighbour_sol
                fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
                list_of_list_of_critical_position = list(dict_of_position.values())
                current_critical_position = list_of_list_of_critical_position[0]
                # print("current critical postion ", current_critical_position)
                # print("new changed sol", local_initial_sol)
                q = 0
            else:
                q = q + 1
                # print("local initial sol",local_initial_sol)
        elif q == 2:
            # print("q ki value", q)
            j = G_Local[a][2]
            new_neighbour_sol = swap(local_initial_sol,current_critical_position,j)
            # print("local initial sol", local_initial_sol)
            # print("new neighbour sol", new_neighbour_sol)
            fitness_new_neighbour_sol,dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
            # print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
            fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
            fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
            # print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
            # print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
            if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
                # print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
                # print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
                # print("yes yha change hua hai")
                local_initial_sol = new_neighbour_sol
                fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
                list_of_list_of_critical_position = list(dict_of_position.values())
                current_critical_position = list_of_list_of_critical_position[0]
                # print("current critical postion ", current_critical_position)
                # print("new changed local_initial_sol", local_initial_sol)
                q = 0
            else:
                q = q + 1
                # print("local initial sol", local_initial_sol)
        elif q == 3:
            # print("q ki value", q)
            j = G_Local[a][3]
            new_neighbour_sol = swap(local_initial_sol, current_critical_position, j)
            # print("local initial sol", local_initial_sol)
            # print("new neighbour sol", new_neighbour_sol)
            fitness_new_neighbour_sol, dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
            # print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
            fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
            fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
            # print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
            # print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
            if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
                # print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
                # print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
                # print("yes yha change hua hai")
                local_initial_sol = new_neighbour_sol
                fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
                list_of_list_of_critical_position = list(dict_of_position.values())
                current_critical_position = list_of_list_of_critical_position[0]
                # print("current critical postion ", current_critical_position)
                # print("new changed local_initial_sol", local_initial_sol)
                q = 0
            else:
                q = q + 1
                # print("local initial sol", local_initial_sol)
        # elif q == 4:
#         #     print("q ki value", q)
        #     j = G_Local[a][2]
        #     new_neighbour_sol = swap(local_initial_sol, current_critical_position, j)
#         #     print("local initial sol", local_initial_sol)
#         #     print("new neighbour sol", new_neighbour_sol)
        #     fitness_new_neighbour_sol, dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
#         #     print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
        #     fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
        #     fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
#         #     print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
#         #     print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
        #     if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
#         #         print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
#         #         print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
#         #         print("yes yha change hua hai")
        #         local_initial_sol = new_neighbour_sol
        #         fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
        #         list_of_list_of_critical_position = list(dict_of_position.values())
        #         current_critical_position = list_of_list_of_critical_position[0]
#         #         print("current critical postion ", current_critical_position)
#         #         print("new changed local_initial_sol", local_initial_sol)
        #         q = 0
        #     else:
        #         q = q + 1
#         #         print("local initial sol", local_initial_sol)
        # elif q == 5:
#         #     print("q ki value", q)
        #     j = G_Local[a][1]
        #     new_neighbour_sol = swap(local_initial_sol, current_critical_position, j)
#         #     print("local initial sol", local_initial_sol)
#         #     print("new neighbour sol", new_neighbour_sol)
        #     fitness_new_neighbour_sol, dict_of_position = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
#         #     print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
        #     fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
        #     fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
#         #     print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
#         #     print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
        #     if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
#         #         print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
#         #         print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
#         #         print("yes yha change hua hai")
        #         local_initial_sol = new_neighbour_sol
        #         fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
        #         list_of_list_of_critical_position = list(dict_of_position.values())
        #         current_critical_position = list_of_list_of_critical_position[0]
#         #         print("current critical postion ", current_critical_position)
#         #         print("new changed local_initial_sol", local_initial_sol)
        #         q = 0
        #     else:
        #         q = q + 1
#         #         print("local initial sol", local_initial_sol)
        # elif q == 6:
#         #     print("q ki value", q)
        #     j = 1
        #     new_neighbour_sol = insertion(local_initial_sol,j)
#         #     print("local initial sol", local_initial_sol)
#         #     print("new neighbour sol", new_neighbour_sol)
        #     fitness_new_neighbour_sol = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
#         #     print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
        #     fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
        #     fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
#         #     print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
#         #     print("fitness local_initial_sol vlaue", fitness_local_initial_sol_value)
        #     if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
#         #         print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
#         #         print("fitness_initial_sol_value", fitness_local_initial_sol_value)
#         #         print("yes yha change hua hai")
        #         local_initial_sol = new_neighbour_sol
        #         fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
#         #         print("new changed sollocal_initial_sol", local_initial_sol)
        #         q = 0
        #     else:
        #         q = q + 1
#         #         print("local initial sol", local_initial_sol)
        # elif q == 7:
#         #     print("q ki value", q)
        #     j = G_Local[a]
        #     new_neighbour_sol = swap(local_initial_sol,j)
#         #     print("local initial sol", local_initial_sol)
#         #     print("new neighbour sol", new_neighbour_sol)
        #     fitness_new_neighbour_sol = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
#         #     print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
        #     fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
        #     fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
#         #     print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
#         #     print("fitness local_initial_sol_vlaue", fitness_local_initial_sol_value)
        #     if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
#         #         print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
#         #         print("fitness_initial_sol_value", fitness_local_initial_sol_value)
#         #         print("yes yha change hua hai")
        #         local_initial_sol = new_neighbour_sol
        #         fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
#         #         print("new changed local_initial_sol", local_initial_sol)
        #         q = 0
        #     else:
        #         q = q + 1
#         #         print("local initial sol", local_initial_sol)
        # elif q == 8:
#         #     print("q ki value", q)
        #     j = 1
        #     new_neighbour_sol = reverse(local_initial_sol,j)
#         #     print("local initial sol", local_initial_sol)
#         #     print("new neighbour sol", new_neighbour_sol)
        #     fitness_new_neighbour_sol = manoj_code(new_neighbour_sol, no_jobs, no_of_machine)
#         #     print("fitness_new_neighbour_sol", fitness_new_neighbour_sol)
        #     fitness_new_neighbour_sol_value_list = list(fitness_new_neighbour_sol.values())
        #     fitness_new_neighbour_sol_value = fitness_new_neighbour_sol_value_list[0]
#         #     print("fitness_new ngiehgbour sol value", fitness_new_neighbour_sol_value)
#         #     print("fitness initial sol local_initial_solvlaue", fitness_local_initial_sol_value)
        #     if fitness_new_neighbour_sol_value < fitness_local_initial_sol_value:
#         #         print("fitness_new_neighbour_sol_value", fitness_new_neighbour_sol_value)
#         #         print("fitness_initial_sol_value", fitness_local_initial_sol_value)
#         #         print("yes yha change hua hai")
        #         local_initial_sol = new_neighbour_sol
        #         fitness_local_initial_sol_value = fitness_new_neighbour_sol_value
#         #         print("new changed local_initial_sol", local_initial_sol)
        #         q = 0
        #     else:
        #         q = q + 1
    #     #         print("local initial sol", local_initial_sol)
    # print("local_initial_sol",local_initial_sol)
    local_initial_sol_join =' '.join([str(elem) for elem in local_initial_sol])
    # print("fitness_local_initial_sol_value", fitness_local_initial_sol_value)
    final_dict_of_position[local_initial_sol_join] = current_critical_position
    return local_initial_sol_join,fitness_local_initial_sol_value,final_dict_of_position

# mylist = [1,1,2,3,3,2,2]
#
# f = local_search(mylist)

