import random
import math
import copy
from SECOND_FJSP_SDST_only import manoj_code

class PSO():

    def __init__(self,no_jobs, no_of_machine,inertia_factor, cognition_factor, social_factor,r, list_of_string_sol_pair, list_of_p_best=[],g_best = 0):
        self.no_jobs = no_jobs
        self.no_of_machine = no_of_machine
        self.inertia_factor = inertia_factor
        self.cognition_factor = cognition_factor
        self.social_factor = social_factor
        self.r = r
        self.list_of_string_sol_pair = list_of_string_sol_pair
        self.list_of_p_best = list_of_p_best
        self.g_best = g_best

    def initialization(self):
        if self.r == 0:
            self.list_of_p_best = self.list_of_string_sol_pair
            list_of_best_vector = sorted(self.list_of_string_sol_pair, key=lambda agent: agent[1])
            # print("list_of_best_vector", list_of_best_vector)
            best_string = list_of_best_vector[0]
            min_makespan = best_string[1]
            best_sequence = copy.deepcopy(best_string[0])
            # print("best sequence", best_sequence)
            self.g_best = best_string
            print("p_best", self.list_of_p_best)
            print("g best", self.g_best)
        else:
            i = 0
            # print("r is more or equal to one>>>>>>>>>>>", self.r)
            # print("g best",self.g_best)
            min_makespan = self.g_best[1]
            # print("min makespan",min_makespan)
            for each in self.list_of_string_sol_pair:
                if each[1]< min_makespan:
                    min_index = i
                    min_makespan = each[1]
                    best_sequence = copy.deepcopy(each[0])
                    # print("best sequence", best_sequence)
                    self.g_best = each
                    # print("self.g_best",self.g_best)
                if each[1] < self.list_of_p_best[i][1]:
                    # print("self.list_of_p_best[i]______________1",self.list_of_p_best[i])
                    self.list_of_p_best[i] = each
                    # print("self.list_of_p_best[i]______________2", self.list_of_p_best[i])
                    # breakpoint()
                i += 1
        # print("change happend>>>>>>>>>>>>>>>>>>>>")
        # print("p_best", self.list_of_p_best)
        # print("g best", self.g_best)
        # print("length of the list of string", self.list_of_string_sol_pair)
        # breakpoint()
        return self.list_of_p_best, self.g_best

# self.current_v[i] = self.current_v[i] + alph*(self.pbest[i]-self.solutions[i]) + best(self.gbest - self.solutions[i])
    def inertial_func(self):
        # print("Mutation Function")
        list_of_p_best, g_best =  self.initialization()
        # print("list of p best",list_of_p_best)
        # print("g nest", g_best)
        # print("length of the list of string", len(self.list_of_string_sol_pair))
        # breakpoint()
        # print("all childs ", all_childs)
        final_childs = []
        inertia_sol_dict = {}
        # print("len of the list of stirng sol pair",len(self.list_of_string_sol_pair))
        i = 0
        each_dict = {}
        for every in self.list_of_string_sol_pair:
            # print("new one>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # print("every",every)
            every_sep = every[0].split(" ")
            # print("every_Sep",every_sep)
            randgroup = []
            x = random.randint(0, len(every_sep) - 1)
            randgroup.append(x)
            for i in range(len(every_sep)):
                y = random.randint(0, len(every_sep) - 1)
                if every_sep[x] != every_sep[y]:
                    randgroup.append(y)
                    break
            # print("randgroup",randgroup)
            z = random.random()
            # print(z)
            # print("self.inertial factor",self.inertia_factor)
            # breakpoint()
            if z < self.inertia_factor:
                # print(z)
                ch = every_sep[randgroup[0]]
                # print("ch",ch)
                ch1 = every_sep[randgroup[1]]
                # print("ch1",ch1)
                every_sep.pop(randgroup[0])
                every_sep.insert(randgroup[0], ch1)
                every_sep.pop(randgroup[1])
                every_sep.insert(randgroup[1], ch)
                # print("every_sep",every_sep)
                # print(every, "mutation hua")
                # every_with_sol = manoj_code_1(self.no_jobs, self.no_of_machine, every_sep)
                every_int= [int(ele) for ele in every_sep]
                # print("each int",every_int)
                each_makespan  = manoj_code(self.no_jobs, self.no_of_machine, every_int)
                each_dict.update(each_makespan)
                makespan_list = list(each_dict.items())
                # print("makespan list",makespan_list)
                min_tuple = makespan_list[0]
                # print("minvalue", min_tuple)
                if min_tuple[1] < self.list_of_p_best[i][1]:
                    # print("self.list_of_p_best[i]______________1",self.list_of_p_best[i])
                    self.list_of_p_best[i] = min_tuple
                    # print("self.list_of_p_best[i]______________2", self.list_of_p_best[i])
                    # breakpoint()
                # list_one = list(two_string_dict.items())
                # inertia_sol_dict.update(every_with_sol)
            else:
                every_sep = every_sep = every[0].split(" ")
                print(every_sep)
            i +=1
            final_childs.append(every_sep)
        # print("final mutate childs",final_childs)
        # print("length of final_child",len(final_childs))
        final_list_of_string = []
        for each in final_childs:
            each_string = " ".join([str(el) for el in each])
            # print("each",each_string)
            final_list_of_string.append(each_string)
        # print("final list of string",final_list_of_string)
        # print("len of the list of stirng sol pair", len(self.list_of_string_sol_pair))
        return final_list_of_string, list_of_p_best, g_best


    def cognition_func(self):
        # population1,population2 = get_population(self.list_os,self.list_ms,self.list_sum)
        new_inertia_child_sol_pair_list, list_of_p_best, g_best = self.inertial_func()
        # print("list of p best", list_of_p_best)
        # print("g best", g_best)
        # print("length of new_inertia_child_sol_pair_list",len(new_inertia_child_sol_pair_list))
        # breakpoint()
        population = new_inertia_child_sol_pair_list
        # print("population>>>>>>>>>", population)
        # print("list of p best",list_of_p_best)
        cross_p_best_sol_list= []
        m = 0
        for each in population:
#             # breakpoint()
            z = random.random()
            # print("z ki value", z)
            if z < self.cognition_factor:
                list_of_childs = []
                two_string_dict = {}
                parent1 = list(each.split(" "))
                # print("parent1", parent1)
                # print(each)
                parent2 = list(list_of_p_best[m][0].split(" "))
                # print("parent2", parent2)
                child1 = []
                child2 = []
                set_of_jobs = set(parent1)
                # print(set_of_jobs)
                list_of_jobs = list(set_of_jobs)
                list_of_jobs = []
                for each_p in parent1:  # for geting total job nos in list of jobs
                    if each_p not in list_of_jobs:
                        list_of_jobs.append(each_p)
                # print("list_of_jobs", list_of_jobs)
                list1_of_jobs = random.sample(list_of_jobs,int(len(list_of_jobs) / 2))  # to get some jobs in list1 and others in list2
                list2_of_jobs = []
                for eac in list_of_jobs:  # to get other jobs not present in list 1
                    if eac not in list1_of_jobs:
                        list2_of_jobs.append(eac)
                # print("list1 jobs", list1_of_jobs)
                # print("list 2 jobs", list2_of_jobs)
                # k = random.randint(1, int(len(parent1) / 2))  # to get random value to be
                # print("k", k)
                i = 0
                l = 0
                for each_1 in parent1:
                    # print("each1", each_1)
                    if each_1 not in list1_of_jobs:  # it is to find each sequence in parent1 whether it is in list1 or not. ifit is in list1,
                        # .........................then no change in place and if it is in list2 then change in place
                        # print("each", each_1)
                        # print("l", l)
                        # print("i", i)
                        parent1.pop(i)
                        # print("parent1.....", parent1)
                        for j in range(len(parent2)):
                            if parent2[l] not in list1_of_jobs:  # will check each seq of job in parent 2 to cross the job nos
                                ch = parent2[l]
                                print(ch)
                                parent1.insert(i, ch)
                                l = l + 1
                                # print("parent1 changed", parent1)
                                break
                            else:
                                l = l + 1
                                continue
                        i = i + 1# to make continuation of i for each value of parent1
                    else:
                        i = i + 1
                        continue
                # print("parent1 final", parent1)
                i_1 = 0
                l_1 = 0
                parent1_2 = list(each.split(" "))
                # print("parent2",parent2)
                # print("parent1_2",parent1_2)
                for each1 in parent2:
                    # print("each1", each1)
                    if each1 not in list1_of_jobs:
                        # print("each", each1)
                        # print("l", l_1)
                        # print("i", i_1)
                        parent2.pop(i_1)
                        # print("parent2.....", parent2)
                        for j in range(len(parent1_2)):
                            if parent1_2[l_1] not in list1_of_jobs:
                                ch = parent1_2[l_1]
                                print(ch)
                                parent2.insert(i_1, ch)
                                l_1 = l_1 + 1
                                # print("parent2 changed", parent2)
                                # print("l1",l_1)
                                break
                            else:
                                l_1 = l_1 + 1
                                continue
                        i_1 = i_1 + 1
                    else:
                        i_1 = i_1 + 1
                        continue
                # print("parent2 final", parent2)
                list_of_childs.append(parent1)
                list_of_childs.append(parent2)
                # print("list_of_childs",list_of_childs)
                for each_c in list_of_childs:
                    each_in= [int(ele) for ele in each_c]
                    # print("each int",each_in)
                    each_makespan  = manoj_code(self.no_jobs, self.no_of_machine, each_in)
                    two_string_dict.update(each_makespan)
                makespan_list = list(two_string_dict.values())
                min_value = min(makespan_list)
                # print("two_string",two_string_dict)
                # print("minvalue", min_value)
                list_one = list(two_string_dict.items())
                # print("list_one",list_one)
                if len(list_one)>1:
                    if list_one[0][1] < list_one[1][1]:
                        cross_p_best_sol_list.append(list_one[0])
                    elif list_one[0][1] > list_one[1][1]:
                        cross_p_best_sol_list.append(list_one[1])
                    else:
                        cross_p_best_sol_list.append(random.choice(list_one))
                else:
                    cross_p_best_sol_list.append(list_one[0])
                # print("list of cross p best sol ", cross_p_best_sol_list)
                m+=1
            else:
                each_sep = each.split(" ")
                each_in = [int(el) for el in each_sep]
                each_makespan = manoj_code(self.no_jobs, self.no_of_machine, each_in)
                list_makespan = list(each_makespan.items())
                # print(list_makespan)
                cross_p_best_sol_list.append(list_makespan[0])
                m += 1
        # print("list of childs_os", cross_p_best_sol_list)
        # print("length of list",len(cross_p_best_sol_list))
        # print("g best",g_best)
        return cross_p_best_sol_list, list_of_p_best, g_best

    def social_func(self):
        # population1,population2 = get_population(self.list_os,self.list_ms,self.list_sum)
        new_cognition_child_sol_pair_list, list_of_p_best, g_best = self.cognition_func()
        # print("list of p best", list_of_p_best)
        # print("g nest", g_best)
        # print("length of new_coginution child sol pair list",len(new_cognition_child_sol_pair_list))
        # breakpoint()
        population_social = new_cognition_child_sol_pair_list
        # print("population_____>>>>social____>>>>>", population_social)
        # print("list of g best", g_best)
        cross_g_best_sol_list = []
        m = 0
        for each in population_social:
#             # breakpoint()
            z = random.random()
            # print("z ki value",z)
            if  z < self.social_factor:
                list_of_childs = []
                two_string_dict = {}
                parent1 = list(each[0].split(" "))
                # print("parent1", parent1)
                # print(each)
                parent2 = list(g_best[0].split(" "))
                # print("parent2", parent2)
                child1 = []
                child2 = []
                set_of_jobs = set(parent1)
                # print(set_of_jobs)
                # list_of_jobs = list(set_of_jobs)
                list_of_jobs = []
                for each_p in parent1:  # for geting total job nos in list of jobs
                    if each_p not in list_of_jobs:
                        list_of_jobs.append(each_p)
                # print("list_of_jobs", list_of_jobs)
                list1_of_jobs = random.sample(list_of_jobs, int(len(
                    list_of_jobs) / 2))  # to get some jobs in list1 and others in list2
                list2_of_jobs = []
                for each_l in list_of_jobs:  # to get other jobs not present in list 1
                    if each_l not in list1_of_jobs:
                        list2_of_jobs.append(each_l)
                # print("list 1 jobs", list1_of_jobs)
                # print("list 2 jobs", list2_of_jobs)
                k = random.randint(1, int(len(parent1) / 2))  # to get random value to be
                # print("k", k)
                i = 0
                l = 0
                for each_p1 in parent1:
                    # print("each1", each_p1)
                    if each_p1 not in list1_of_jobs:  # it is to find each sequence in parent1 whether it is in list1 or not. ifit is in list1,
                        # .........................then no change in place and if it is in list2 then change in place
                        # print("each", each_p1)
                        # print("l", l)
                        # print("i", i)
                        parent1.pop(i)
                        # print("parent1.....", parent1)
                        for j in range(len(parent2)):
                            if parent2[l] not in list1_of_jobs:  # will check each seq of job in parent 2 to cross the job nos
                                ch = parent2[l]
                                # print(ch)
                                parent1.insert(i, ch)
                                l = l + 1
                                # print("parent1 changed", parent1)
                                break
                            else:
                                l = l + 1
                                continue
                        i = i + 1  # to make continuation of i for each value of parent1
                    else:
                        i = i + 1
                        continue
                # print("parent1 final", parent1)
                i_1 = 0
                l_1 = 0
                parent1 = list(each[0].split(" "))
                for each_p2 in parent2:
                    # print("each1", each_p2)
                    if each_p2 not in list1_of_jobs:
                        # print("each", each_p2)
                        # print("l", l_1)
                        # print("i", i_1)
                        parent2.pop(i_1)
                        # print("parent2.....", parent2)
                        for j in range(len(parent1)):
                            if parent1[l_1] not in list1_of_jobs:
                                ch = parent1[l_1]
                                # print(ch)
                                parent2.insert(i_1, ch)
                                l_1 = l_1 + 1
                                # print("parent2 changed", parent2)
                                break
                            else:
                                l_1 = l_1 + 1
                                continue
                        i_1 = i_1 + 1
                    else:
                        i_1 = i_1 + 1
                        continue
                    # print("parent2 final", parent2)
                list_of_childs.append(parent1)
                list_of_childs.append(parent2)
                # print("list_of_childs", list_of_childs)
                for each_c in list_of_childs:
                    each_in = [int(ele) for ele in each_c]
                    # print("each int", each_in)
                    each_makespan = manoj_code(self.no_jobs, self.no_of_machine, each_in)
                    two_string_dict.update(each_makespan)
                makespan_list = list(two_string_dict.values())
                min_value = min(makespan_list)
                # print(min_value)
                list_two = list(two_string_dict.items())
                # print("list_two",list_two)
                if len(list_two)>1:
                    if list_two[0][1] < list_two[1][1]:
                        cross_g_best_sol_list.append(list_two[0])
                    elif list_two[0][1] > list_two[1][1]:
                        cross_g_best_sol_list.append(list_two[1])
                    else:
                        cross_g_best_sol_list.append(random.choice(list_two))
                else:
                    cross_g_best_sol_list.append(list_two[0])
                # print("list of cross g best osl ",cross_g_best_sol_list)
                m+=1
            else:
                each_sep = each[0].split(" ")
                each_in = [int(el) for el in each_sep]
                each_makespan = manoj_code(self.no_jobs, self.no_of_machine, each_in)
                list_makespan = list(each_makespan.items())
                print(list_makespan)
                cross_g_best_sol_list.append(list_makespan[0])
                m += 1
        # print("list of g best childs_os", cross_g_best_sol_list)
        # print("length of g best list_of_childs_ms", len(cross_g_best_sol_list))
        # print("length of list of p best",len(list_of_p_best))
        # print("value of g_best",g_best)
        if len(cross_g_best_sol_list) <10 or len(list_of_p_best) <10:
            # print("stop beacause the lenth is short")
            breakpoint()
        # breakpoint()
        return cross_g_best_sol_list, list_of_p_best, g_best

        #
# ga = gentic_algorithm(['1 1 2 3 3 2 2', '3 2 1 1 3 2 2', '1 3 2 3 2 2 1', '1 3 3 2 1 2 2', '2 3 2 1 3 2 1', '2 3 2 3 1 2 1', '3 3 1 1 2 2 2', '2 2 2 3 3 1 1', '1 1 2 3 3 2 2', '1 1 2 3 2 3 2'])
# ga.Mutation()

