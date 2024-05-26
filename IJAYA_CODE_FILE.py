import random
import math
from IJAYA_manojpalcode_21_08 import manojpal_code_1
import itertools as it


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
            "6": 100,
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
setup_table = {
    "0": {
        "0": {
            "0": 1,
            "1": 2,
            "2": 1,
            "3": 6,
            "4": 1,
            "5": 3,
            "6": 2,
            "7": 5,
            "8": 9,
            "9": 5
        },
        "1": {
            "0": 1,
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 5,
            "5": 3,
            "6": 100,
            "7": 1,
            "8": 11,
            "9": 3
        },
        "2":{
            "0": 3,
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 4,
            "5": 6,
            "6": 6,
            "7": 3,
            "8": 3,
            "9": 3
        },

    },
    "1": {
        "0": {
            "0": 2,
            "1": 3,
            "2": 4,
            "3": 3,
            "4": 5,
            "5": 1,
            "6": 2,
            "7": 1,
            "8": 4,
            "9": 4
        },
        "1": {
            "0": 2,
            "1": 8,
            "2": 6,
            "3": 1,
            "4": 9,
            "5": 5,
            "6": 1,
            "7": 6,
            "8": 3,
            "9": 1
        },
        "2":{
            "0": 6,
            "1": 10,
            "2": 2,
            "3": 6,
            "4": 1,
            "5": 3,
            "6": 1,
            "7": 7,
            "8": 6,
            "9": 1
        },
    },
    "2": {
        "0": {
            "0": 1,
            "1": 3,
            "2": 7,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 3,
            "7": 1,
            "8": 1,
            "9": 1
        },
        "1": {
            "0": 7,
            "1": 3,
            "2": 3,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 1,
            "8": 7,
            "9": 2
        },
        "2":{
            "0": 2,
            "1": 1,
            "2": 6,
            "3": 5,
            "4": 3,
            "5": 2,
            "6": 1,
            "7": 2,
            "8": 1,
            "9": 1
        }
    },
    "3": {
        "0": {
            "0": 5,
            "1": 8,
            "2": 5,
            "3": 1,
            "4": 6,
            "5": 2,
            "6": 1,
            "7": 5,
            "8": 1,
            "9": 5
        },
        "1": {
            "0": 1,
            "1": 2,
            "2": 1,
            "3": 7,
            "4": 5,
            "5": 3,
            "6": 1,
            "7": 1,
            "8": 4,
            "9": 2
        },
        "2":{
            "0": 2,
            "1": 2,
            "2": 8,
            "3": 1,
            "4": 5,
            "5": 2,
            "6": 4,
            "7": 3,
            "8": 4,
            "9": 2
        },
    },
    "4": {
        "0": {
            "0": 2,
            "1": 1,
            "2": 2,
            "3": 2,
            "4": 4,
            "5": 3,
            "6": 1,
            "7": 7,
            "8": 2,
            "9": 3
        },
        "1": {
            "0": 2,
            "1": 5,
            "2": 2,
            "3": 9,
            "4": 2,
            "5": 2,
            "6": 7,
            "7": 6,
            "8": 1,
            "9": 1
        },
        "2":{
            "0": 6,
            "1": 1,
            "2": 2,
            "3": 1,
            "4": 9,
            "5": 1,
            "6": 2,
            "7": 11,
            "8": 8,
            "9": 6
        }
    },
    "5": {
        "0":{
            "0": 5,
            "1": 1,
            "2": 1,
            "3": 8,
            "4": 1,
            "5": 2,
            "6": 6,
            "7": 2,
            "8": 2,
            "9": 10
        },
        "1": {
            "0": 3,
            "1": 3,
            "2": 3,
            "3": 5,
            "4": 1,
            "5": 2,
            "6": 3,
            "7": 6,
            "8": 1,
            "9": 13
        },
        "2":{
            "0": 1,
            "1": 4,
            "2": 3,
            "3": 6,
            "4": 2,
            "5": 3,
            "6": 1,
            "7": 5,
            "8": 1,
            "9": 7
        }
    },
    "6": {
        "0": {
            "0": 1,
            "1": 3,
            "2": 5,
            "3": 1,
            "4": 2,
            "5": 2,
            "6": 4,
            "7": 6,
            "8": 7,
            "9": 4
        },
        "1": {
            "0": 2,
            "1": 8,
            "2": 1,
            "3": 2,
            "4": 2,
            "5": 2,
            "6": 8,
            "7": 2,
            "8": 1,
            "9": 1
        },
        "2":{
            "0": 2,
            "1": 1,
            "2": 2,
            "3": 1,
            "4": 2,
            "5": 1,
            "6": 6,
            "7": 1,
            "8": 5,
            "9": 2
        },
    },
    "7": {
        "0": {
            "0": 3,
            "1": 4,
            "2": 2,
            "3": 3,
            "4": 2,
            "5": 5,
            "6": 1,
            "7": 2,
            "8": 5,
            "9": 6
        },
        "1": {
            "0": 2,
            "1": 1,
            "2": 3,
            "3": 2,
            "4": 4,
            "5": 4,
            "6": 2,
            "7": 6,
            "8": 4,
            "9": 4
        },
        "2":{
            "0": 3,
            "1": 1,
            "2": 13,
            "3": 3,
            "4": 4,
            "5": 2,
            "6": 4,
            "7": 2,
            "8": 2,
            "9": 3
        },
    },
    "8": {
        "0": {
            "0": 3,
            "1": 8,
            "2": 1,
            "3": 1,
            "4": 2,
            "5": 1,
            "6": 1,
            "7": 4,
            "8": 1,
            "9": 2
        },
        "1": {
            "0": 4,
            "1": 6,
            "2": 2,
            "3": 2,
            "4": 1,
            "5": 3,
            "6": 1,
            "7": 6,
            "8": 2,
            "9": 6
        },
        "2":{
            "0": 1,
            "1": 2,
            "2": 2,
            "3": 3,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 3,
            "8": 4,
            "9": 11
        },
    },
    "9": {
        "0": {
            "0": 2,
            "1": 3,
            "2": 1,
            "3": 3,
            "4": 4,
            "5": 1,
            "6": 1,
            "7": 4,
            "8": 19,
            "9": 1
        },
        "1": {
            "0": 2,
            "1": 1,
            "2": 2,
            "3": 1,
            "4": 8,
            "5": 2,
            "6": 1,
            "7": 2,
            "8": 8,
            "9": 1
        },
        "2":{
            "0": 1,
            "1": 1,
            "2": 3,
            "3": 2,
            "4": 1,
            "5": 3,
            "6": 2,
            "7": 3,
            "8": 1,
            "9": 20
        },
    }
}
Transport_Table = {
    "0": {
            "0": 0,
            "1": 4,
            "2": 2,
            "3": 1,
            "4": 5,
            "5": 1,
            "6": 2,
            "7": 1,
            "8": 5,
            "9": 5
        },
    "1": {
            "0": 1,
            "1": 0,
            "2": 5,
            "3": 1,
            "4": 5,
            "5": 2,
            "6": 5,
            "7": 5,
            "8": 1,
            "9": 5
        },
    "2": {
            "0": 1,
            "1": 3,
            "2": 0,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 5,
            "8": 5,
            "9": 4
        },
    "3":{
            "0": 3,
            "1": 1,
            "2": 3,
            "3": 0,
            "4": 1,
            "5": 4,
            "6": 3,
            "7": 3,
            "8": 4,
            "9": 1
        },
    "4":{
            "0": 4,
            "1": 2,
            "2": 5,
            "3": 3,
            "4": 0,
            "5": 1,
            "6": 4,
            "7": 1,
            "8": 3,
            "9": 2
        },
    "5":{
            "0": 5,
            "1": 5,
            "2": 1,
            "3": 1,
            "4": 2,
            "5": 0,
            "6": 3,
            "7": 2,
            "8": 3,
            "9": 2
        },
    "6":{
            "0": 1,
            "1": 1,
            "2": 2,
            "3": 5,
            "4": 2,
            "5": 5,
            "6": 0,
            "7": 3,
            "8": 2,
            "9": 4
        },
    "7":{
            "0": 3,
            "1": 5,
            "2": 1,
            "3": 5,
            "4": 5,
            "5": 4,
            "6": 2,
            "7": 0,
            "8": 3,
            "9": 1
        },
    "8":{
            "0": 3,
            "1": 3,
            "2": 1,
            "3": 3,
            "4": 1,
            "5": 3,
            "6": 2,
            "7": 3,
            "8": 0,
            "9": 4
        },
    "9":{
            "0": 1,
            "1": 5,
            "2": 5,
            "3": 3,
            "4": 1,
            "5": 3,
            "6": 3,
            "7": 2,
            "8": 5,
            "9": 0
        }
}
list_generated = []



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
        print(operation_time_list)
    return operation_time_list

def machine_available_list(no_jobs, operation_nos_list):
    string_position_list = []
    for each1 in operation_nos_list:
        each_list = []
        for eacher in range(each1):
            each_list.append(eacher)
        string_position_list.append(each_list)
    print("string position", string_position_list)
    machine_available_dict = {}
    q = 0
    for each in range(no_jobs):  ### To get operation time matrix ########
        i = 0
        while i < operation_nos_list[each]:  ###
            all_list = []
            print("i ki value", i)
            print("each", each)
            mach_time_duration = operation_table[str(each)][str(i)]
            i = i + 1
            print(mach_time_duration.values())
            each_list_value = list(mach_time_duration.values())
            each_list_key = list(mach_time_duration.keys())
            print(each_list_value)
            l = 0
            for each_1 in each_list_value:
                if each_1>1000:
                    each_list_key.pop(l)
                    l = l+1
            all_list.append(each_list_key)
            print("all list", all_list)
            machine_available_dict[q] = all_list
            q+=1
    print(machine_available_dict)
    return machine_available_dict

# function = machine_available_list(4, [3,3,4,2])
def findmin(list_sum):
    if len(list_sum) == 1:
        return list_sum[0]
    else:
        return min(list_sum[0],findmin(list_sum[1:]))

def tournament_selection(final_pair_list,y):
    population_list = final_pair_list.copy()
    # print("populaito list",population_list)
    list_of_best_parents = []
    for i in range(y):
        parents = random.choices(population_list, k=5)
        print("parents",parents)
        parents_sorted = sorted(parents, key=lambda agent: agent[1][0])
        print("parente sorted",parents_sorted)
        best_parent = parents_sorted[0]
        list_of_best_parents.append(best_parent)
        population_list.remove(best_parent)
        print("best parent",best_parent)
    return list_of_best_parents

def local_search_1(parent, machine_avail_list, no_jobs,operation_no_list): # Local search for critical operations
    os_seq_list = []
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1) + str(h + 1))
        j += 1
    print(os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    while True:
        crit_opn = random.choice(parent[1][4])
        print(crit_opn)
        list_crit = crit_opn.split("+")
        job_opr_no = list_crit[0]+list_crit[1]
        k = 0
        for each in os_seq_list:
            if each == job_opr_no:
                pos = k
                mach_list = machine_avail_list[pos]
            k += 1
        print(pos)
        mach_no = final_parent_ms[pos]
        if len(machine_avail_list) == 1:
            continue
        else:
            print("mach list", mach_list)
            if str(int(mach_no) - 1) in mach_list[0]:
                mach_list[0].remove(str(int(mach_no) - 1))
            new_mach = str(int(random.choice(mach_list[0])) + 1)
            print("new mach", new_mach)
            final_parent_ms.pop(pos)
            final_parent_ms.insert(pos, new_mach)
            break
    print(final_parent_ms)
    return final_parent_os,final_parent_ms


def local_search_2(parent, machine_avail_list, no_jobs,operation_no_list):# Local search for a random critical operations
    os_seq_list = []
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1) + str(h + 1))
        j += 1
    print(os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    while True:
        crit_opn = random.choice(parent[1][4])
        print(crit_opn)
        list_crit = crit_opn.split("+")
        job_opr_no = list_crit[0] + list_crit[1]
        print(job_opr_no)
        print("mach no", mach_no)
        k = 0
        for each in os_seq_list:
            if each == job_opr_no:
                pos = k
                mach_list = machine_avail_list[pos]
            k += 1
        print(pos)
        mach_no = final_parent_ms[pos]
        if len(machine_avail_list) == 1:
            continue
        else:
            print("mach list", mach_list)
            if str(int(mach_no) - 1) in mach_list[0]:
                mach_list[0].remove(str(int(mach_no) - 1))
            new_mach = str(int(random.choice(mach_list[0])) + 1)
            print("new mach", new_mach)
            final_parent_ms.pop(pos)
            final_parent_ms.insert(pos, new_mach)
            break
    print(final_parent_ms)
    return final_parent_os,final_parent_ms

def local_search_3(parent, machine_avail_list, no_jobs,operation_no_list,no_of_machine):# Local search for a random critical operattion
    os_seq_list = []
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1) + str(h + 1))
        j += 1
    print(os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    # while True:
    list_of_jobs = []
    dict_of_mach = {}
    for key in range(no_of_machine):
        dict_of_mach[str(key + 1)] = []
    print("dict_of_mach", dict_of_mach)
    for each in parent[1][4]:
        print(each)
        list_each = each.split("+")
        job_opr_no = list_each[0] + list_each[1]
        mach_no = list_each[2]
        dict_of_mach[mach_no].append(job_opr_no)
    print(dict_of_mach)
    list_of_mach = []
    for key, value in dict_of_mach.items():
        if len(value) > 1:
            list_of_mach.extend(value)
        if list_of_mach == [] and len(value)==1:
            list_of_mach.extend(value)
            break
    print("list of machine", list_of_mach)
    # pos = 0
    while True:
        job_no = random.choice(list_of_mach)
        print(job_no)
        k = 0
        for each1 in os_seq_list:
            if each1 == job_no:
                pos = k
                mach_list = machine_avail_list[k]
                print("mach_list",mach_list)
            k += 1
        print(pos)
        mach_no = final_parent_ms[pos]
        if len(machine_avail_list) == 1:
            continue
        else:
            print("mach list", mach_list)
            if str(int(mach_no) - 1) in mach_list[0]:
                mach_list[0].remove(str(int(mach_no) - 1))
            new_mach = str(int(random.choice(mach_list[0])) + 1)
            print("new mach", new_mach)
            final_parent_ms.pop(pos)
            final_parent_ms.insert(pos, new_mach)
            break
    print(final_parent_ms)
    return final_parent_os, final_parent_ms

def local_search_5(parent, machine_avail_list, no_jobs,operation_no_list):#Local search for a random critical machine
    os_seq_list = []
    print("machine_avail_list")
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1) + str(h + 1))
        j += 1
    print(os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    while True:
        crit_opn = random.choice(parent[1][5])
        print(crit_opn)
        list_crit = crit_opn.split("+")
        job_opr_no = list_crit[0] + list_crit[1]
        print(job_opr_no)
        print("mach no", mach_no)
        k = 0
        for each in os_seq_list:
            if each == job_opr_no:
                pos = k

                mach_list = machine_avail_list[pos]
                print("mach_list", mach_list)
            k += 1
        print(pos)
        mach_no = final_parent_ms[pos]
        if len(machine_avail_list) == 1:
            continue
        else:
            print("mach list", mach_list)
            if str(int(mach_no) - 1) in mach_list[0]:
                mach_list[0].remove(str(int(mach_no) - 1))
            new_mach = str(int(random.choice(mach_list[0])) + 1)
            print("new mach", new_mach)
            final_parent_ms.pop(pos)
            final_parent_ms.insert(pos, new_mach)
            break
    print(final_parent_ms)
    return final_parent_os, final_parent_ms

def local_search_6(parent, machine_avail_list, no_jobs,operation_no_list): # Local search for a random operation
    os_seq_list = []
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1) + str(h + 1))
        j += 1
    print(os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    while True:
        pos = random.randint(0, len(os_seq_list) - 1)
        print("pos", pos)
        k = 0
        mach_no = final_parent_ms[pos]
        print(mach_no)
        for each in os_seq_list:
            if k == pos:
                mach_list = machine_avail_list[pos]
                print("mach_list", mach_list)
            k += 1
        if len(machine_avail_list) == 1:
            continue
        else:
            print("mach list", mach_list)
            if str(int(mach_no) - 1) in mach_list[0]:
                mach_list[0].remove(str(int(mach_no) - 1))
            new_mach = str(int(random.choice(mach_list[0])) + 1)
            print("new mach", new_mach)
            final_parent_ms.pop(pos)
            final_parent_ms.insert(pos, new_mach)
            break
    print(final_parent_ms)
    return final_parent_os, final_parent_ms

def local_search_7(parent, machine_avail_list, no_jobs,operation_no_list,operation_time_list): # Local search for random operation with minimum processing machine
    os_seq_list = []
    j = 0
    for each in range(no_jobs):
        for h in range(operation_no_list[j]):
            os_seq_list.append(str(each + 1)+"+"+str(h + 1))
        j += 1
    print("os seq_list",os_seq_list)
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    crit_opn = random.choice(os_seq_list)
    list_crit = crit_opn.split("+")
    job_no = list_crit[0]
    opr_no = list_crit[1]
    job_opr_no = list_crit[0] +"+"+ list_crit[1]
    print(crit_opn)
    print("job no", job_no)
    print(opr_no)
    print(job_opr_no)
    operation_no = opr_no
    list_time = operation_time_list[int(job_no) - 1][int(operation_no) - 1]
    a = min(list_time)
    print("a", a)
    list_mach_same = []
    new = 0
    for each in list_time:
        if each == a:
            list_mach_same.append(str(new + 1))
        new += 1
    print(list_mach_same)
    mach_no = random.choice(list_mach_same)
    print(mach_no)
    k = 0
    for each in os_seq_list:
        if each == job_opr_no:
            pos = k
        k += 1
    print("pos", pos)
    k = 0
    final_parent_ms.pop(pos)
    final_parent_ms.insert(pos, mach_no)
    print(final_parent_ms)
    return final_parent_os, final_parent_ms

def insertion(parent):
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    randgroup = []
    # print(critical_position)
    x = random.randint(0, len(final_parent_os) - 1)
    randgroup.append(x)
    while True:
        y = random.randint(0, len(final_parent_os) - 1)
        if y not in randgroup and final_parent_os[x] != final_parent_os[y]:
            randgroup.append(y)
            break
        else:
            continue
    print("randgroup", randgroup)
    job_no = final_parent_os[x]
    print("job no", job_no)
    k = 0
    sequence_mach = []
    for each1 in final_parent_os:
        if each1 == job_no:
            sequence_mach.append(final_parent_ms[k])
        k += 1
    print("seqeunce_mach", sequence_mach)
    ch = final_parent_os[randgroup[0]]
    final_parent_os.pop(randgroup[0])
    final_parent_ms.pop(randgroup[0])
    final_parent_os.insert(randgroup[1], ch)
    final_parent_ms.insert(randgroup[1], ch)
    print("final_parent_os", final_parent_os)
    m = 0
    n = 0
    for each2 in final_parent_os:
        if each2 == job_no:
            final_parent_ms[m] = sequence_mach[n]
            n += 1
        m += 1
    print("final parent ms", final_parent_ms)
    return final_parent_os, final_parent_ms

def swap(parent):
    print("parent", parent)
    pr1 = parent[0].split("+")
    print("pr1",pr1)
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    randgroup = []
    # print(critical_position)
    x = random.randint(0, len(final_parent_os) - 1)
    randgroup.append(x)
    while True:
        y = random.randint(0, len(final_parent_os) - 1)
        if y not in randgroup and final_parent_os[x] != final_parent_os[y]:
            randgroup.append(y)
            break
        else:
            continue
    print("randgroup", randgroup)
    job_no1 = final_parent_os[x]
    print("job no1", job_no1)
    job_no2 = final_parent_os[y]
    print("job no2", job_no2)
    k = 0
    sequence_mach1 = []
    sequence_mach2 = []
    for each1 in final_parent_os:
        if each1 == job_no1:
            sequence_mach1.append(final_parent_ms[k])
        if each1 == job_no2:
            sequence_mach2.append(final_parent_ms[k])
        k += 1
    print("seqeunce_mach1", sequence_mach1)
    print("seqeunce_mach2", sequence_mach2)
    ch = final_parent_os[randgroup[0]]
    ch1 = final_parent_os[randgroup[1]]
    final_parent_os.pop(randgroup[0])
    final_parent_ms.pop(randgroup[0])
    final_parent_os.insert(randgroup[0], ch1)
    final_parent_ms.insert(randgroup[0], ch1)
    final_parent_os.pop(randgroup[1])
    final_parent_ms.pop(randgroup[1])
    final_parent_os.insert(randgroup[1], ch)
    final_parent_ms.insert(randgroup[1], ch)
    print("final_parent_os", final_parent_os)
    m = 0
    n = 0
    p = 0
    for each2 in final_parent_os:
        if each2 == job_no1:
            final_parent_ms[m] = sequence_mach1[n]
            n += 1
        if each2 == job_no2:
            final_parent_ms[m] = sequence_mach2[p]
            p += 1
        m += 1
    print("final parent ms", final_parent_ms)
    return final_parent_os, final_parent_ms

def reverse(parent):
    pr1 = parent[0].split("+")
    final_parent_os = pr1[0].split(" ")
    final_parent_ms = pr1[1].split(" ")
    print("final_parent_os", final_parent_os)
    print("final parent ms", final_parent_ms)
    randgroup = []
    # print(critical_position)
    x = random.randint(0, len(final_parent_os) - 1)
    randgroup.append(x)
    while True:
        y = random.randint(0, len(final_parent_os) - 1)
        if y not in randgroup and final_parent_os[x] != final_parent_os[y]:
            randgroup.append(y)
            break
        else:
            continue
    print("randgroup", randgroup)
    job_no1 = final_parent_os[x]
    print("job no1", job_no1)
    job_no2 = final_parent_os[y]
    print("job no2", job_no2)
    k = 0
    sequence_mach1 = []
    sequence_mach2 = []
    for each1 in final_parent_os:
        if each1 == job_no1:
            sequence_mach1.append(final_parent_ms[k])
        if each1 == job_no2:
            sequence_mach2.append(final_parent_ms[k])
        k += 1
    print("seqeunce_mach1", sequence_mach1)
    print("seqeunce_mach2", sequence_mach2)
    randgroup1 = randgroup.copy()
    randgroup.sort(reverse=True)
    randgroup1.sort()
    print(randgroup1)
    print(randgroup)
    if randgroup[1] == 0:
        new_parent_os = final_parent_os[randgroup[0]::-1]
        new_parent_ms = final_parent_ms[randgroup[0]::-1]

        print("new final parent os", new_parent_os)
        print("new final parent ms", new_parent_ms)
    else:
        new_parent_os = final_parent_os[randgroup[0]:randgroup[1] - 1:-1]
        new_parent_ms = final_parent_ms[randgroup[0]:randgroup[1] - 1:-1]
        print("new final parent os", new_parent_os)
        print("new final parent ms", new_parent_ms)
    j = 0
    for i in range(randgroup1[0], randgroup1[1] + 1):
        final_parent_os.pop(i)
        final_parent_ms.pop(i)
        final_parent_os.insert(i, new_parent_os[j])
        final_parent_ms.insert(i, new_parent_ms[j])
        j = j + 1
    print("final parent os", final_parent_os)
    print("final_parent_ms", final_parent_ms)
    m = 0
    n = 0
    p = 0
    for each2 in final_parent_os:
        if each2 == job_no1:
            final_parent_ms[m] = sequence_mach1[n]
            n += 1
        if each2 == job_no2:
            final_parent_ms[m] = sequence_mach2[p]
            p += 1
        m += 1
    print("final parent ms", final_parent_ms)

    return final_parent_os, final_parent_ms


class Improved_jaya_algorithm:

    def __init__(self,list_os_ms, list_sol, no_of_machine,no_jobs,operation_nos_list):
        self.list_os_ms = list_os_ms
        self.list_sol = list_sol
        self.no_of_machine = no_of_machine
        self.no_jobs = no_jobs
        self.operation_no_list = operation_nos_list

    def Routing_local_search(self):
        n = 0
        final_pair_list = []
        for each_os_ms in self.list_os_ms:
            os_ms_pair = []
            each_sum = self.list_sol[n]
            os_ms_pair.append(each_os_ms)
            os_ms_pair.append(each_sum)
            os_ms_pair_tuple = tuple(os_ms_pair)
            final_pair_list.append(os_ms_pair_tuple)
            n = n + 1
        print("final_pair_list", final_pair_list)

        sorted_final_pair_list = sorted(final_pair_list, key=lambda agent: agent[1][0])

        population = final_pair_list
        each_best = sorted_final_pair_list[0]
        print(each_best)
        best_solution = []
        best_result = each_best[1][0]
        # for each in final_pair_list:
        #     if each[1][3] == best_result:
        best_solution.append(each_best)
        print("best solution",best_solution)
        print("best result", best_result)
        operation_time_list = operation_time_list_method(self.no_jobs,self.operation_no_list)
        print("operation time list",operation_time_list)
        new_population = []
        for each in population:
            new_list = []
            new_list.append(each)
            new_list.extend(best_solution)
            new_each = random.choice(new_list)
            if new_each[1][0]< each[1][0]:
                each = new_each
            else:
                print("new_each",new_each)
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os,new_solution_ms = local_search_1(new_each, machine_avail_list,self.no_jobs,self.operation_no_list)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,new_solution_os,new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_1(new_each, machine_avail_list,self.no_jobs,self.operation_no_list)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,new_solution_os, new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_3(new_each, machine_avail_list,self.no_jobs, self.operation_no_list, self.no_of_machine)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,new_solution_os, new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_3(new_each, machine_avail_list,
                                                                                self.no_jobs, self.operation_no_list, self.no_of_machine)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,
                                                       new_solution_os, new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_5(new_each, machine_avail_list,
                                                                                self.no_jobs, self.operation_no_list)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,
                                                       new_solution_os, new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_6(new_each, machine_avail_list,
                                                                                self.no_jobs, self.operation_no_list)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,
                                                       new_solution_os, new_solution_ms)
                print(each_dict_string_sol)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
                new_solution_os, new_solution_ms = local_search_7(new_each, machine_avail_list,
                                                                                self.no_jobs, self.operation_no_list,operation_time_list)
                each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,
                                                       new_solution_os, new_solution_ms)
                original_sol = []
                for key, value in each_dict_string_sol.items():
                    original_sol.append(key)
                    original_sol.append(value)
                original_sol_tup = tuple(original_sol)
                if original_sol_tup[1][0] < new_each[1][0]:
                    new_each = original_sol_tup
                print(new_each)
                print(best_solution[0])
                ###update the best solution wite new each######
                if new_each[1][0]< best_solution[0][1][0]:
                    print("earlier",best_solution)
                    best_solution[0] = new_each
                    print("later",best_solution)
                each = new_each
            new_population.append(each)
        return new_population,best_solution,final_pair_list
    def Scheduling_local_search(self):
        new_routing_list, best_solution,final_pair_list = self.Routing_local_search()
        n = 0
        population= new_routing_list
        final_population = []
        for new_each in best_solution:
            # breakpoint()
            random_list = [1,2,3]
            chance = random.choice(random_list)
            if chance ==1:
                final_parent_os, final_parent_ms = reverse(new_each)
            elif chance ==2:
                final_parent_os, final_parent_ms = swap(new_each)
            elif chance ==3:
                final_parent_os, final_parent_ms = insertion(new_each)
            rand_list1 = random.randint(0, len(final_parent_ms) - 1)
            machine_avail_list = machine_available_list(self.no_jobs, self.operation_no_list)
            machine_change_list = machine_avail_list[rand_list1]
            # print("machine_change_list",machine_change_list)
            # print("machine no to be alreaday have", final_parent_ms[rand_list1])
            mach_no =  final_parent_ms[rand_list1]
            machine_change_list[0].remove(str(int(mach_no)-1))
            machine_tobe_change = random.choice(machine_change_list[0])
            final_parent_ms.pop(rand_list1)
            final_parent_ms.insert(rand_list1, str(int(machine_tobe_change)+1))
            print(final_parent_ms)
            each_dict_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,final_parent_os, final_parent_ms)
            original_sol = []
            for key, value in each_dict_string_sol.items():
                original_sol.append(key)
                original_sol.append(value)
            final_each_sol = tuple(original_sol)
            print(final_each_sol)
            final_population.append(final_each_sol)
        final_population.extend(population)
        print("list of childs_os", list_of_childs_os)
        print("length of list_of_childs_ms",len(list_of_childs_os))
        # breakpoint()
        return final_population,final_pair_list

    def Simulated_annealing(self):
        final_sol_list,original_pair_list = self.Scheduling_local_search()
        list_of_value = []
        for eac in final_sol_list:
            pr1 = eac[0].split("+")
            mutate_os_string = pr1[0].split(" ")
            # print("mutate os string", mutate_os_string)
            mutate_ms_string = pr1[1].split(" ")
            initial_sol = eac[1][0]
            initial_sol_ful = eac[1]
            i = 0
            T = 0.4
            total_final_list = []
            operation_time_list = operation_time_list_method(self.no_jobs, self.operation_no_list)
            # print("operation time list", operation_time_list)
            total_sum  = 0
            for every1 in operation_time_list[0]:
                sum1 = sum(every1)
                total_sum = total_sum + sum1
            # print("total sum", total_sum)
#             breakpoint()
            while i < 4:
                new_mutate_os_string,new_mutate_ms_string = insertion(eac)
                # print("new_mutate_os_string", new_mutate_os_string)
                # print("new_ms_string_list", new_mutate_ms_string)
                each_dict_ms_string_sol = manojpal_code_1(self.no_jobs, self.operation_no_list, self.no_of_machine,
                                                          new_mutate_os_string, new_mutate_ms_string)
                # print("each_dict_ms_string_sol",each_dict_ms_string_sol)
                each_dict_ms_string_value = list(each_dict_ms_string_sol.values())
                new_solution = each_dict_ms_string_value[0][0]
                final_solution = each_dict_ms_string_value[0]
                delta = new_solution - initial_sol
                print(delta)
                T = (T * total_sum) / (self.no_jobs * self.no_of_machine * 10)
                print(T)
                z = random.random()
                # print(z)
                # breakpoint()
                if new_solution < initial_sol:
                    mutate_os_string = new_mutate_os_string
                    mutate_ms_string = new_mutate_ms_string
                    initial_sol = new_solution
                    initial_sol_ful = final_solution
                else:
                    sim_annealing = math.exp(-delta / T)
                    if  sim_annealing >= z:
                        mutate_os_string = new_mutate_os_string
                        mutate_ms_string = new_mutate_ms_string
                        initial_sol = new_solution
                        initial_sol_ful = final_solution
                i = i + 1
            final_mutate_os_string = " ".join([ele for ele in mutate_os_string])
            final_mutate_ms_string = " ".join([ele for ele in mutate_ms_string])
            total_final_list.append(final_mutate_os_string + "+" + final_mutate_ms_string)
            total_final_list.append(initial_sol_ful)
            print(total_final_list)
            total_final_tuple = tuple(total_final_list)
            # use similar method like local search as we defined
            list_of_value.append(total_final_tuple)
            print(list_of_value)
            # print("each", eac)
        list_of_value.extend(original_pair_list)
        print("list_of_value",list_of_value)
        print("length of solution", len(list_of_value))
        sorted_list_of_value = sorted(list_of_value, key=lambda agent: agent[1][0])
        print("sorted list of vlaue",sorted_list_of_value)
        final_list_data = sorted_list_of_value[:100]
        print("final list data",final_list_data)
        print("length of final list data", len(final_list_data))
        # breakpoint()
        return final_list_data
