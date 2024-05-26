import random
import math
import itertools as it
Maintenance_Tasks = {
    "0": {"aks": 8,
          "akl": 12,
          "tij": 1
          },
    "1": {"aks": 9,
          "akl": 12,
          "tij": 1
          },
    "2": {"aks": 0,
          "akl": 6,
          "tij": 1
          },
    "3": {"aks": 2,
          "akl": 7,
          "tij": 1
          },
    "4": {"aks": 0,
          "akl": 7,
          "tij": 1
          },
    "5": {"aks": 7,
          "akl": 10,
          "tij": 1
          },
    "6": {"aks": 0,
          "akl": 9,
          "tij": 1
          },
    "7": {"aks": 2,
          "akl": 9,
          "tij": 1
          },
    "8": {"aks": 1,
          "akl": 9,
          "tij": 1
          },
    "9": {"aks": 4,
          "akl": 8,
          "tij": 1
          }
}
operation_table = {
    "0": {
        "0": {
            "0": 1,
            "1": 4,
            "2": 6,
            "3": 9,
            "4": 3,
            "5": 5,
            "6": 2,
            "7": 8,
            "8": 9,
            "9": 5

        },
        "1": {
            "0": 4,
            "1": 1,
            "2": 1,
            "3": 3,
            "4": 4,
            "5": 8,
            "6": 10,
            "7": 4,
            "8": 11,
            "9": 4
        },
        "2": {
            "0": 3,
            "1": 2,
            "2": 5,
            "3": 1,
            "4": 5,
            "5": 6,
            "6": 9,
            "7": 5,
            "8": 10,
            "9": 3
        }
    },
    "1": {
        "0": {
            "0": 2,
            "1": 10,
            "2": 4,
            "3": 5,
            "4": 9,
            "5": 8,
            "6": 4,
            "7": 15,
            "8": 8,
            "9": 4
        },
        "1": {
            "0": 4,
            "1": 8,
            "2": 7,
            "3": 1,
            "4": 9,
            "5": 6,
            "6": 1,
            "7": 10,
            "8": 7,
            "9": 1
        },
        "2": {
            "0": 6,
            "1": 11,
            "2": 2,
            "3": 7,
            "4": 5,
            "5": 3,
            "6": 5,
            "7": 14,
            "8": 9,
            "9": 2
        }
    },
    "2": {
        "0": {
            "0": 8,
            "1": 5,
            "2": 8,
            "3": 9,
            "4": 4,
            "5": 3,
            "6": 5,
            "7": 3,
            "8": 8,
            "9": 1
        },
        "1": {
            "0": 9,
            "1": 3,
            "2": 6,
            "3": 1,
            "4": 2,
            "5": 6,
            "6": 4,
            "7": 1,
            "8": 7,
            "9": 2
        },
        "2": {
            "0": 7,
            "1": 1,
            "2": 8,
            "3": 5,
            "4": 4,
            "5": 9,
            "6": 1,
            "7": 2,
            "8": 3,
            "9": 4
        }
    },
    "3": {
        "0": {
            "0": 5,
            "1": 10,
            "2": 6,
            "3": 4,
            "4": 9,
            "5": 5,
            "6": 1,
            "7": 7,
            "8": 1,
            "9": 6
        },
        "1": {
            "0": 4,
            "1": 2,
            "2": 3,
            "3": 8,
            "4": 7,
            "5": 4,
            "6": 6,
            "7": 9,
            "8": 8,
            "9": 4
        },
        "2": {
            "0": 7,
            "1": 3,
            "2": 12,
            "3": 1,
            "4": 6,
            "5": 5,
            "6": 8,
            "7": 3,
            "8": 5,
            "9": 2
        }
    },
    "4": {
        "0": {
            "0": 7,
            "1": 10,
            "2": 4,
            "3": 5,
            "4": 6,
            "5": 3,
            "6": 5,
            "7": 15,
            "8": 2,
            "9": 6
        },
        "1": {
            "0": 5,
            "1": 6,
            "2": 3,
            "3": 9,
            "4": 8,
            "5": 2,
            "6": 8,
            "7": 6,
            "8": 1,
            "9": 7
        },
        "2": {
            "0": 6,
            "1": 1,
            "2": 4,
            "3": 1,
            "4": 10,
            "5": 4,
            "6": 3,
            "7": 11,
            "8": 13,
            "9": 9
        }
    },
    "5":{
        "0": {
            "0": 8,
            "1": 9,
            "2": 10,
            "3": 8,
            "4": 4,
            "5": 2,
            "6": 7,
            "7": 8,
            "8": 3,
            "9": 10
        },
        "1": {
            "0": 7,
            "1": 3,
            "2": 12,
            "3": 5,
            "4": 4,
            "5": 3,
            "6": 6,
            "7": 9,
            "8": 2,
            "9": 15
        },
        "2": {
            "0": 4,
            "1": 7,
            "2": 3,
            "3": 6,
            "4": 3,
            "5": 4,
            "6": 1,
            "7": 5,
            "8": 1,
            "9": 11
        }
    },
    "6":{
        "0": {
            "0": 1,
            "1": 7,
            "2": 8,
            "3": 3,
            "4": 4,
            "5": 9,
            "6": 4,
            "7": 13,
            "8": 10,
            "9": 7
        },
        "1": {
            "0": 3,
            "1": 8,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 6,
            "6": 11,
            "7": 2,
            "8": 13,
            "9": 3
        },
        "2": {
            "0": 5,
            "1": 4,
            "2": 2,
            "3": 1,
            "4": 2,
            "5": 1,
            "6": 8,
            "7": 14,
            "8": 5,
            "9": 7
        }
    },
    "7":{
        "0": {
            "0": 5,
            "1": 7,
            "2": 11,
            "3": 3,
            "4": 2,
            "5": 9,
            "6": 8,
            "7": 5,
            "8": 12,
            "9": 8
        },
        "1": {
            "0": 8,
            "1": 3,
            "2": 10,
            "3": 7,
            "4": 5,
            "5": 13,
            "6": 4,
            "7": 6,
            "8": 8,
            "9": 4
        },
        "2": {
            "0": 6,
            "1": 2,
            "2": 13,
            "3": 5,
            "4": 4,
            "5": 3,
            "6": 5,
            "7": 7,
            "8": 9,
            "9": 5
        }
    },
    "8":{
        "0": {
            "0": 3,
            "1": 9,
            "2": 1,
            "3": 3,
            "4": 8,
            "5": 1,
            "6": 6,
            "7": 7,
            "8": 5,
            "9": 4
        },
        "1": {
            "0": 4,
            "1": 6,
            "2": 2,
            "3": 5,
            "4": 7,
            "5": 3,
            "6": 1,
            "7": 9,
            "8": 6,
            "9": 7
        },
        "2": {
            "0": 8,
            "1": 5,
            "2": 4,
            "3": 8,
            "4": 6,
            "5": 1,
            "6": 2,
            "7": 3,
            "8": 10,
            "9": 12
        }
    },
    "9":{
        "0": {
            "0": 4,
            "1": 3,
            "2": 1,
            "3": 6,
            "4": 7,
            "5": 1,
            "6": 2,
            "7": 6,
            "8": 20,
            "9": 6
        },
        "1": {
            "0": 3,
            "1": 1,
            "2": 8,
            "3": 1,
            "4": 9,
            "5": 4,
            "6": 1,
            "7": 4,
            "8": 17,
            "9": 15
        },
        "2": {
            "0": 9,
            "1": 2,
            "2": 4,
            "3": 2,
            "4": 3,
            "5": 5,
            "6": 2,
            "7": 4,
            "8": 10,
            "9": 23
        }
    }
}
def machine_selection_method(operation_no_list,no_of_machine,no_jobs):
    machine_selection_list = []
    operation_nos_list= operation_no_list.copy()
    sum_of_opers = sum(operation_nos_list)
    final_mach_list = []
    i = 0
    for each in range(no_jobs):
        for each_12 in range(operation_nos_list[i]):
            mach_list = []
            for mach_no in range(no_of_machine):
                xx = operation_table[str(each)][str(each_12)][str(mach_no)]
#                 # print("xx",xx)
                if xx != 499:
                    mach_list.append(mach_no+1)
            final_mach_list.append(mach_list)
        i +=1
#     # print("mach list", mach_list)
#     # print(" final mach list", final_mach_list)
    return final_mach_list

def encoder_os_sequence(operation_start_time_list):
    x_stl = operation_start_time_list
    # print(x_stl)
    # x_stl = [0,21,33,51,0,114,132,156,0,21,47,94,16,32,82,114]
    x_seq = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
    # x_seq = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4]
    temp = sorted(zip(x_stl,x_seq),key = lambda x: x[0])
    x_stl =  [x[0] for x in temp]
    x_seq = [x[1] for x in temp]
    # print(x_stl)
    # print(x_seq)
    final_os_seq =  ' '.join([str(elem) for elem in x_seq])
    # print("final_os_seq", final_os_seq)
    # breakpoint()
    return final_os_seq





def operation_time_list_method(no_jobs,operation_nos_list):
    operation_time_list = []
    for each in range(no_jobs):  ### To get operation time matrix ########
        i = 0
        all_list = []
        while i < operation_nos_list[each]:  ###
            # print("i ki value", i)
            # print("each", each)
            mach_time_duration = operation_table[str(each)][str(i)]
            i = i + 1
            # print(mach_time_duration.values())
            each_list = list(mach_time_duration.values())
            all_list.append(each_list)
            # print("all list", all_list)
        operation_time_list.append(all_list)
        # print(operation_time_list)
    return operation_time_list


def tournament_selection(final_pair_list,y):
    population_list = final_pair_list.copy()
    # print("populaito list",population_list)
    list_of_best_parents = []
    for i in range(y):
        parents = random.choices(population_list, k=5)
        # print("parents",parents)
        parents_sorted = sorted(parents, key=lambda agent: agent[1])
        # print("parente sorted",parents_sorted)
        best_parent = parents_sorted[0]
        list_of_best_parents.append(best_parent)
        population_list.remove(best_parent)
        # print("best parent",best_parent)
    return list_of_best_parents

def get_population(list_of_os_ms_parents,list_sum):

    n = 0
    final_pair_list = []
    for each_os_ms in list_of_os_ms_parents:
        os_ms_pair = []
        each_sum = list_sum[n]
        os_ms_pair.append(each_os_ms)
        os_ms_pair.append(each_sum)
        os_ms_pair_tuple = tuple(os_ms_pair)
        final_pair_list.append(os_ms_pair_tuple)
        n=n+1
    # print("final_pair_list",final_pair_list)
    #######################################
    y = int(len(final_pair_list))
    list_of_selected_parents = tournament_selection(final_pair_list,y)
    # print(list_of_selected_parents)
    ############################################
    # list_of_selected_parents = random.sample(list_of_parents, 16)
    # print("list of selected parents", list_of_selected_parents)
    population = list_of_selected_parents
    # print("population",population)
    list_of_parents1 = list_of_selected_parents.copy()
    matching_pair = list(it.combinations(list_of_selected_parents, 2))
    list_of_matching_pair = []
    # print(matching_pair)
    matching_pair1 = matching_pair.copy()
    try:
        for each in matching_pair:
            match1 = each[0]
            match2 = each[1]
            if match1 in list_of_parents1 and match2 in list_of_parents1:
                list_of_matching_pair.append(each)
                matching_pair1.remove(each)
                list_of_parents1.remove(match1)
                list_of_parents1.remove(match2)
                # print(list_of_matching_pair)
            else:
                pass
    except ValueError:
        pass
    # print("list_of matchig pair",list_of_matching_pair)
    # breakpoint()
    list_of_os_ms_pair = []
    list_of_sum = []
    list_of_os_ms = []
    for ech in list_of_matching_pair:
        os_tuple = (ech[0][0], ech[1][0])
        list_of_os_ms_pair.append(os_tuple)
        list_of_os_ms.append(ech[0][0])
        list_of_os_ms.append(ech[1][0])
        list_of_sum.append(ech[0][1])
        list_of_sum.append(ech[1][1])
    # print("list_of_os_ms_pair",list_of_os_ms_pair)
    # print("list_of_os_ms", list_of_os_ms)
    # print("list_of_sum",list_of_sum)
    # print("length of list_of_os_pair", len(list_of_os_ms))
    # print("length of list_of_sum", len(list_of_sum))
    # breakpoint()
    return list_of_os_ms_pair,list_of_os_ms,list_of_sum

class genetic_algorithm:

    def __init__(self,list_os_ms_pair,list_sol, no_of_machine,no_jobs,operation_nos_list):
        self.list_os_ms_pair = list_os_ms_pair
        self.list_sol = list_sol
        self.no_of_machine = no_of_machine
        self.no_jobs = no_jobs
        self.operation_no_list = operation_nos_list

    def Crossover_os(self):
        # population1,population2 = get_population(self.list_os,self.list_ms,self.list_sum)
        population_os_ms_pair, list_of_os_ms, list_of_sum = get_population(self.list_os_ms_pair, self.list_sol)
        # population_os_ms_pair = self.list_os_ms_pair
        # print("list",len(self.list_os_ms_pair))
        population = population_os_ms_pair
        # print("population>>>>>>>>>", population)
        list_of_childs_os_ms = []
        # breakpoint()
        original_population_list = []
        i12= 0
        for each in population:
            # breakpoint()
            original_os_ms1 = []
            original_os_ms2 = []
            list_a = each[0].split("+")
            # print("list_a", list_a)
            list_b = each[1].split("+")
            # print("list_b", list_b)
            pr1_a = list_a[0] # a for only OS start time string of parent 1
            pr1_b = list_a[1] # b for only MS start time string of parent 1
            pr2_a = list_b[0] # a for only OS start time string of parent 2
            pr2_b = list_b[1] # b for only OS start time string of parent 2
            parent1_a = list(pr1_a.split(" "))
            parent2_a = list(pr2_a.split(" "))
            # print(parent1_a)
            # print(parent2_a)
            parent1_b = list(pr1_b.split(" "))
            parent2_b = list(pr2_b.split(" "))
            # print(parent1_b)
            # print(parent2_b)
            original_os_ms1.append(parent1_a)
            original_os_ms1.append(parent1_b)
            original_os_ms2.append(parent2_a)
            original_os_ms2.append(parent2_b)
            original_population_list.append(original_os_ms1)
            original_population_list.append(original_os_ms2)
            # print(original_population_list)
            child_os_ms_pair_1 = []
            child_os_ms_pair_2 = []
            parent1_a_copy = parent1_a.copy()
            parent1_b_copy = parent1_b.copy()
            parent2_a_copy = parent2_a.copy()
            parent2_b_copy = parent2_b.copy()
            # print("parent1_a_copy", parent1_a_copy)
            # print("parent1_b_copy", parent1_b_copy)
            # print("parent2_a_copy",parent2_a_copy)
            # print("parent2_a_copy",parent2_b_copy)
            z  = random.random()
            # print("z",z)
            if z <= 0.3: # one cut point crossover probability
                # print("pair", i12)
                rand_no = random.randint(1,len(parent1_b)-2)
                z_1 = random.random()
                if z_1 <=0.5: # for crosover of Os start time String
                    # print(parent1_a)
                    # print(parent2_a)
                    child1_a = parent1_a[0:rand_no] + parent2_a[rand_no:]
                    # print("parent1_a_cross", child1_a)
                    child2_a = parent2_a[0:rand_no] + parent1_a[rand_no:]
                    # print("parent2_a_cross", child2_a)
                    child_os_ms_pair_1.append(child1_a)
                    child_os_ms_pair_1.append(parent1_b)
                    child_os_ms_pair_2.append(child2_a)
                    child_os_ms_pair_2.append(parent2_b)
                else:           # for crossover of MS string
                    # print(parent1_b)
                    # print(parent2_b)
                    child1_b = parent1_b[0:rand_no] + parent2_b[rand_no:]
                    # print("child1 b", child1_b)
                    child2_b = parent2_b[0:rand_no] + parent1_b[rand_no:]
                    # print("child2 b", child2_b)
                    child_os_ms_pair_1.append(parent1_a)
                    child_os_ms_pair_1.append(child1_b)
                    child_os_ms_pair_2.append(parent2_a)
                    child_os_ms_pair_2.append(child2_b)
                list_of_childs_os_ms.append(child_os_ms_pair_1)
                list_of_childs_os_ms.append(child_os_ms_pair_2)
                # print("list_of_childs_os_ms..1", list_of_childs_os_ms)
                i12 = i12+1
            elif z > 0.3 and z <= 0.5: # uniform crossover probability
                # print("pair", i12)
                rand_list = []
                for i_1 in range(2):
                    rand_no = random.randint(1,len(parent1_b)-2)
                    rand_list.append(rand_no)
                    # print("rnad list", rand_list)
                for each in rand_list:
                    parent1_a_copy.pop(each)
                    parent1_a_copy.insert(each, parent2_a[each])
                    parent1_b_copy.pop(each)
                    parent1_b_copy.insert(each, parent2_b[each])
                    parent2_a_copy.pop(each)
                    parent2_a_copy.insert(each, parent1_a[each])
                    parent2_b_copy.pop(each)
                    parent2_b_copy.insert(each, parent1_b[each])
                child_os_ms_pair_1.append(parent1_a_copy)
                child_os_ms_pair_1.append(parent1_b_copy)
                child_os_ms_pair_2.append(parent2_a_copy)
                child_os_ms_pair_2.append(parent2_b_copy)
                # print("child_os_ms_pair_1", child_os_ms_pair_1)
                # print("child_os_ms_pair_2", child_os_ms_pair_2)
                list_of_childs_os_ms.append(child_os_ms_pair_1)
                list_of_childs_os_ms.append(child_os_ms_pair_2)
                # print("list_of_childs_os_ms..2", list_of_childs_os_ms)
                i12 = i12+1
        # print("list of childs_os....", list_of_childs_os_ms)
        # print("length of list_of_childs_ms..3", len(list_of_childs_os_ms))
        # breakpoint()
        return list_of_childs_os_ms, original_population_list

    # for each in fitness:
    #     population_cum_prob = population_cum_prob + each
    #     list_population_cum_prob.append(population_cum_prob)
    def Mutation_OS(self):
        # print("IGA MUTATION FUNCTION")
        no_jobs = self.no_jobs
        operation_no_list = self.operation_no_list
        no_of_machine = self.no_of_machine
        list_of_cross_os_ms_strings, population_os_ms_pair = self.Crossover_os()
        # print("listof cross os strings", list_of_cross_os_ms_strings)
        machine_available_list = machine_selection_method(operation_no_list, no_of_machine,no_jobs)
        # print("machine avaialble list", machine_available_list)
        list_of_mutation = []
        for each in list_of_cross_os_ms_strings:
            z = random.random()
            list_of_mutation_string = []
            if z < 0.1:
                parent1_os = each[0]
                parent1_ms = each[1]
                rand_list1 = random.randint(0,len(parent1_ms)-1)
                machine_change_list = machine_available_list[rand_list1]
                machine_tobe_change = random.choice(machine_change_list)
                parent1_ms.pop(rand_list1)
                parent1_ms.insert(rand_list1, machine_tobe_change)
                # print(parent1_ms)
                randgroup1 = []
                for i_3 in range(2):
                    rand_list2 = random.randint(0,len(parent1_ms)-2)
                    randgroup1.append(rand_list2)
                # print("randgroup1", randgroup1)
                parent1_os.pop(randgroup1[0])
                parent1_os.insert(randgroup1[0],parent1_os[randgroup1[1]])
                parent1_os.pop(randgroup1[1])
                parent1_os.insert(randgroup1[1],parent1_os[randgroup1[0]])
                # print(parent1_os)
                list_of_mutation_string.append(parent1_os)
                list_of_mutation_string.append(parent1_ms)
                list_of_mutation.append(list_of_mutation_string)
            else:
                list_of_mutation.append(each)
        # print(list_of_mutation)
        list_os_ms_pair = []
        # print("asfsf", list_of_mutation)
        # print(population_os_ms_pair)
        # print(len(population_os_ms_pair))
        list_of_mutation.extend(population_os_ms_pair)
        # breakpoint()
        # print("sfsf", list_of_mutation)
        for each in list_of_mutation:
            # print(each[0])
            operation_sequence_string = encoder_os_sequence([int(elem) for elem in each[0]])
            machine_selection_string = ' '.join([str(elem) for elem in each[1]])
            list_os_ms_pair.append([operation_sequence_string +"+"+machine_selection_string])
        return list_os_ms_pair

        # breakpoint()
        #
#         # print("total_final_dict", total_final_dict)
        # list_of_value = []
        # for key, value in total_final_dict.items():
        #     list_of_each = []
        #     list_of_each.append(key)
        #     list_of_each.append(value)
        #     list_of_value.append(list_of_each)
#         # print("list_of_value", list_of_value)
        # sorted_list_of_value = sorted(list_of_value, key=lambda agent: agent[1][3])
#         # print("sorted list of vlaue", sorted_list_of_value)
        # final_list_data = sorted_list_of_value[:100]
#         # print("final list data", final_list_data)
        # # breakpoint()
        # return final_list_data

        #
# ga = gentic_algorithm(['1 1 2 3 3 2 2', '3 2 1 1 3 2 2', '1 3 2 3 2 2 1', '1 3 3 2 1 2 2', '2 3 2 1 3 2 1', '2 3 2 3 1 2 1', '3 3 1 1 2 2 2', '2 2 2 3 3 1 1', '1 1 2 3 3 2 2', '1 1 2 3 2 3 2'])
# ga.Mutation()

