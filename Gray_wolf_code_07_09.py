import random
import math
import copy
import sys
from Second_bidding_mk_1 import manoj_code_1
from nbd_search_second import Nbd_search
from Local_search_second import local_search

def get_population(list_of_parents_with_makespan,prob_cross):

    list_of_parents_with_makespan1 = list_of_parents_with_makespan.copy()
    # print("list_of_parents_with_makespan1", list_of_parents_with_makespan1)
    list_of_strings = []
    for each in list_of_parents_with_makespan1:
        list_of_strings.append(each[0])
    # print("list of stirngs", list_of_strings)
    # breakpoint()
    y = sorted(list_of_parents_with_makespan, key=lambda item:item[1:])
    # print("y ki vlaue", y)
    # breakpoint()
    list1 = []
    for each in y:
        if each[1:] not in list1:
            list1.append(each[1:])
    # print(list1)
    # breakpoint()
    list_of_one_wolf = []
    list_of_two_wolf = []
    list_of_three_wolf = []
    for each in y:
        if each[1:] == list1[0]:
            list_of_one_wolf.append(each[0])
        elif each[1:] == list1[1]:
            list_of_two_wolf.append(each[0])
        elif each[1:] == list1[2]:
            list_of_three_wolf.append(each[0])
    list_of_one_wolf = sorted(list_of_one_wolf, key=lambda item:item[1:])
    list_of_two_wolf = sorted(list_of_two_wolf, key=lambda item:item[1:])
    list_of_three_wolf = sorted(list_of_three_wolf, key=lambda item:item[1:])
    # print("list_of_one_wolf",list_of_one_wolf)
    # print("list_of_two_wolf",list_of_two_wolf)
    # print("list_of_three_wolf", list_of_three_wolf)
    list_of_alpha_wolf_final = []
    list_of_beta_wolf_final = []
    list_of_delta_wolf_final = []
    # breakpoint()
    if len(list_of_one_wolf) ==1:
        # print("1")
        list_of_alpha_wolf_final = [list_of_one_wolf[0]]
        if len(list_of_two_wolf) ==1:
            # print("2")
            list_of_beta_wolf_final = [list_of_two_wolf[0]]
            list_of_delta_wolf_final = [list_of_three_wolf[0]]
        else:
            # print("3")
            list_of_beta_wolf_final = [list_of_two_wolf[0]]
            list_of_delta_wolf_final = [list_of_two_wolf[1]]
    else:
        if len(list_of_one_wolf)==2:
            # print("4")
            list_of_alpha_wolf_final=[list_of_one_wolf[0]]
            list_of_beta_wolf_final = [list_of_one_wolf[1]]
            list_of_delta_wolf_final = [list_of_two_wolf[0]]
        else:
            # print("5")
            list_of_alpha_wolf_final = [list_of_one_wolf[0]]
            list_of_beta_wolf_final = [list_of_one_wolf[1]]
            list_of_delta_wolf_final = [list_of_one_wolf[2]]
    # print("alpha wolf", list_of_alpha_wolf_final)
    # print("beta wolf", list_of_beta_wolf_final)
    # print("delta wolf", list_of_delta_wolf_final)
    # breakpoint()
    # list_of_other_wolf11223 = filter(lambda i:i not in list_of_alpha_wolf,list(list_of_strings))
#     # print("list of other wold",list_of_other_wolf11223[0])
    list_of_other_wolf = []
    for each in list_of_strings:
        if each not in list_of_alpha_wolf_final and each not in list_of_beta_wolf_final and each not in list_of_delta_wolf_final:
            list_of_other_wolf.append(each)
    # print("list_of_other_wolf",list_of_other_wolf)
    list_of_other_wolf1 = list_of_other_wolf.copy()
    # print("list_of_other_wolf",list_of_other_wolf)
    # breakpoint()
    list_of_matching_pair = []
    total_iter = int(prob_cross *len(list_of_strings))
    # print("total iteration",total_iter)
    for i in range(total_iter):
        v = random.choice(list_of_other_wolf1)
        list_of_other_wolf1.remove(v)
        x = random.random()
        matching_pair = []
        if x <= 1 / 3:
            # print("x1",x)
            matching_pair.append(v)
            matching_pair.append(list_of_alpha_wolf_final[0])
            matching_pair1 = tuple(matching_pair)
            list_of_matching_pair.append(matching_pair1)
            # print("1", matching_pair1)
        elif x > 1 / 3 and x < 2 / 3:
            # print("x2",x)
            matching_pair.append(v)
            matching_pair.append(list_of_beta_wolf_final[0])
            matching_pair1 = tuple(matching_pair)
            list_of_matching_pair.append(matching_pair1)
            # print("2", matching_pair1)
        else:
            # print("x3",x)
            matching_pair.append(v)
            matching_pair.append(list_of_delta_wolf_final[0])
            matching_pair1 = tuple(matching_pair)
            list_of_matching_pair.append(matching_pair1)
    #         print("3", matching_pair1)
    # print("list of other wolf original", list_of_other_wolf)
    # print("list of changed wolf", list_of_other_wolf1)

    list_of_selected_parents = []
    for each in list_of_parents_with_makespan1:
        if each[0] not in list_of_other_wolf1:
            list_of_selected_parents.append(each)
    # print("list_of_selected_parents",list_of_selected_parents)
    # print("list_of_matching_pair", list_of_matching_pair)
    # breakpoint()
    return list_of_matching_pair, list_of_selected_parents


class grey_wolf_algorithm:

    def __init__(self,no_jobs,no_of_machine,no_of_population,prob_cross, list_of_parents,list_of_string_sol_pair,final_dict_of_critical_position):
        self.list_of_parents = list_of_parents
        self.no_jobs = no_jobs
        self.no_of_population = no_of_population
        self.no_of_machine = no_of_machine
        self.list_of_string_sol_pair = list_of_string_sol_pair
        self.final_dict_of_critical_position = final_dict_of_critical_position
        self.prob_cross = prob_cross

    def Crossover(self):#Uniform crossover
        population1,parents_sol_pair_list = get_population(self.list_of_string_sol_pair,self.prob_cross)
        # print("parents sol pair list CRossover", parents_sol_pair_list)
        population = population1
        # print("population>>>>>>>>>", population)
        list_of_childs = []
        for each in population:
            pr1 = each[0]
            pr2 = each[1]
            parent1 = list(pr1.split(" "))
            parent2 = list(pr2.split(" "))
            child1 = []
            child2 = []
            for j in range(len(parent1)):
                if j % 2 == 0:
                    child1.append(parent1[j])
            a = -1
            for i in parent2:
                if child1.count(i) < parent2.count(i):
                    child1.insert(a + 2, i)
                a = a + 2
            for j in range(len(parent2)):
                if j % 2 == 0:
                    child2.append(parent2[j])
            a = -1
            for i in parent1:
                if child2.count(i) < parent1.count(i):
                    child2.insert(a + 2, i)
                a = a + 2
            list_of_childs.append(child1)
            list_of_childs.append(child2)
        # print("list_of_childs", list_of_childs)
        new_dict_childs = {}
        final_dict_position_after_cross = {}
        for each in list_of_childs:
            each_dict_string,dict_of_position_after_cross = manoj_code_1(self.no_jobs, self.no_of_machine, each)
            new_dict_childs.update(each_dict_string)
            final_dict_position_after_cross.update(dict_of_position_after_cross)
        new_list_of_childs = list(new_dict_childs.keys())
        new_sol_of_childs = list(new_dict_childs.values())
        # print("new_list_of_childs", new_list_of_childs)
        new_child_sol_pair_list = []
        n = 0
        for each1 in new_list_of_childs:
            string_sol_pair = []
            each_sol_makespan = new_sol_of_childs[n][0]
            each_sol_setup_time = new_sol_of_childs[n][1]
            each_sol_transport_time = new_sol_of_childs[n][2]
            each_sol_sum_three = new_sol_of_childs[n][3]
            string_sol_pair.append(each1)
            string_sol_pair.append(each_sol_makespan)
            string_sol_pair.append(each_sol_setup_time)
            string_sol_pair.append(each_sol_transport_time)
            string_sol_pair.append(each_sol_sum_three)
            string_sol_pair_tuple = tuple(string_sol_pair)
            new_child_sol_pair_list.append(string_sol_pair_tuple)
            n = n + 1
        # print("string sol pair list", new_child_sol_pair_list)
        initial_parents_list = parents_sol_pair_list
        final_parents_child_list = new_child_sol_pair_list + initial_parents_list
        # print("final_parents_child_list", final_parents_child_list)
        return list_of_childs, final_parents_child_list,new_child_sol_pair_list,final_dict_position_after_cross

    def Mutation(self):#adaptive mutation
        # print("Mutation Function")
        all_childs, final_list_cross_childs,sol_all_childs,final_dict_position_after_cross = self.Crossover()#get makespan value from sol all childs and do further iteration
        # print("all childs ", all_childs)
        list_cross_childs= []
        list_childs_makespan = []
        a = []
        # print("sol_all_childs",sol_all_childs)
        # breakpoint()
        for each in sol_all_childs:
            new_each = each[0].split(" ")
            b = [eval(x) for x in new_each]
            list_cross_childs.append(b)
            list_childs_makespan.append(each[1])
        # print("lsit of cross childs",list_cross_childs)
        # breakpoint()
        # print("list_childs_makespan", list_childs_makespan)
        operation_strings_list = list_cross_childs.copy()
        # print("operation_strings_list",operation_strings_list)
        operation_makespan = list_childs_makespan.copy()
        # print("operation_makespan",operation_makespan)
        list_of_fit=[]
        for each in list_childs_makespan:
            fit_func = (100/each)
            list_of_fit.append(fit_func)
        # print("list_of_fit-----",list_of_fit)
        fit_max = max(list_of_fit)
        fit_min = min(list_of_fit)
        list_of_fitness_p = []
        for eac in list_of_fit:
            fitness_p = (1-((fit_max - eac)/(fit_max - fit_min)))
            list_of_fitness_p.append(fitness_p)
            # fitness_func = (100/Cmax)
        #     print("fitness_p",fitness_p)
        # print("list_of_fitness_p",list_of_fitness_p)
        # breakpoint()
        final_childs_of_mutate = []
        mutate_sol_dict = {}
        final_dict_of_position_after_mutation = {}
        for i in range(len(operation_strings_list)):
            every = operation_strings_list[i]
            Mutation_Rate = list_of_fitness_p[i]
            # print("Mutation rate",Mutation_Rate)
            z = random.random()
            # print("z",z)
            if z < Mutation_Rate:
                if Mutation_Rate<0.5:
                    # print("every1",every)
                    q = Nbd_search()
                    every1 = q.swap(every)
                    final_childs_of_mutate.append(every1)
                elif Mutation_Rate>= 0.5 and Mutation_Rate<= 0.8:
                    # print("every2", every)
                    q = Nbd_search()
                    every1 = q.insertion(every)
                    final_childs_of_mutate.append(every1)
                else:
                    # print("every3", every)
                    q = Nbd_search()
                    every1 = q.reverse(every)
                    final_childs_of_mutate.append(every1)
            # else:
#             #     print("every",every)
            #     every1=every.split()
#             #     print("last every1",every1)
            #     final_childs.append(every1)
        # print("final childs_of_mutate", final_childs_of_mutate)
        for each1 in final_childs_of_mutate:
            every_with_sol, dict_of_position_after_mutate = manoj_code_1(self.no_jobs, self.no_of_machine, each1)
            mutate_sol_dict.update(every_with_sol)
            final_dict_of_position_after_mutation.update(dict_of_position_after_mutate)
        new_list_of_mutate_childs = list(mutate_sol_dict.keys())
        new_sol_of_mutate_childs = list(mutate_sol_dict.values())
        # print("new_list_of_mutate childs", new_list_of_mutate_childs)
        new_mutate_child_sol_pair_list = []
        n = 0
        for each1 in new_list_of_mutate_childs:
            string_sol_pair = []
            each_sol_makespan = new_sol_of_mutate_childs[n][0]
            each_sol_setup_time = new_sol_of_mutate_childs[n][1]
            each_sol_transport_time = new_sol_of_mutate_childs[n][2]
            each_sol_sum_three = new_sol_of_mutate_childs[n][3]
            string_sol_pair.append(each1)
            string_sol_pair.append(each_sol_makespan)
            string_sol_pair.append(each_sol_setup_time)
            string_sol_pair.append(each_sol_transport_time)
            string_sol_pair.append(each_sol_sum_three)
            child_sol_pair_tuple = tuple(string_sol_pair)
            new_mutate_child_sol_pair_list.append(child_sol_pair_tuple)
            n = n + 1
        # print("string sol mutate pair list", new_mutate_child_sol_pair_list)
        initial_parents_list = final_list_cross_childs
        final_aftermutate_parents_child_list = new_mutate_child_sol_pair_list + initial_parents_list
        final_dict_of_position = {}
        final_dict_of_position.update(self.final_dict_of_critical_position)
        # print("self fincal dictof ", self.final_dict_of_critical_position)
        # print("final dict of position1", final_dict_of_position)
        final_dict_of_position.update(final_dict_position_after_cross)
        # print("final dict of position2", final_dict_of_position)
        # print("final_dict_position", final_dict_position_after_cross)
        final_dict_of_position.update(final_dict_of_position_after_mutation)
        # print("final dict of position3", final_dict_of_position)
        # print("final dict pos for mutation", final_dict_of_position_after_mutation)
        # print("final_after mutateparents_child_list", final_aftermutate_parents_child_list)
        # print(len(final_aftermutate_parents_child_list))
        list_of_best_strings_mutation = sorted(final_aftermutate_parents_child_list, key=lambda agent: agent[1:])
        # print("list of best strings after mutation", list_of_best_strings_mutation)
        # breakpoint()
        final_list_of_childs_mutation = list_of_best_strings_mutation[:self.no_of_population + 5]
        # print("final_list_of_childs after mutation ", final_list_of_childs_mutation)
        # print(len(final_list_of_childs_mutation))
        each_best = final_list_of_childs_mutation[0]
        best_strings = []
        best_makespan = each_best[1:]
        # print("best_makespan", best_makespan)
        # breakpoint()
        final_list_of_childs_mutation_1 = final_list_of_childs_mutation.copy()
        for each in final_list_of_childs_mutation:
            if each[1:] == best_makespan:
                best_strings.append(each[0])
                final_list_of_childs_mutation_1.remove(each)
        # print("best strings", best_strings)
        # breakpoint()
        ####################
        best_strings_str = []
        for each3 in best_strings:
            new_list = each3.split(" ")
            generated_list = [int(elem) for elem in new_list]
            best_strings_str.append(generated_list)
        # print("best strings str ", best_strings_str)
        # print(len(best_strings_str))
        # breakpoint()
        #################
        final_dict_of_critical_position = {}
        for each1 in best_strings_str:
            # print("len of best string str", len(best_strings_str))
            each1_str = ' '.join([str(elem) for elem in each1])
            # print("each1", each1)
            # print("each1_str", each1_str)
            p, q, r = local_search(each1, self.no_jobs, self.no_of_machine)
            new_best_strings_int_sol = []
            new_best_strings_int_sol.append(p)
            new_best_strings_int_sol.append(q[0])
            new_best_strings_int_sol.append(q[1])
            new_best_strings_int_sol.append(q[2])
            new_best_strings_int_sol.append(q[3])
            new_best_strings_int_sol_tuple = tuple(new_best_strings_int_sol)
            final_list_of_childs_mutation_1.insert(0,new_best_strings_int_sol_tuple)
            final_dict_of_critical_position.update(r)
        # print("Neighbourhood search.......//////", new_best_strings_int_sol)
        # print("new_list__best_solution tuple", new_best_strings_int_sol_tuple)
        # print("final_dict_of_critical_position", final_dict_of_critical_position)
        # print("length of finaldict of critical position", len(final_dict_of_critical_position))
        # breakpoint()
        return final_list_of_childs_mutation_1, final_dict_of_critical_position


# dict_of_parents_with_makespan = {'3 3 1 2 2 1 2': 18.0, '2 3 1 1 2 3 2': 15.0, '2 1 2 3 2 1 3': 16.0, '2 1 2 3 1 2 3': 16.0, '1 3 1 3 2 2 2': 18.0, '3 2 3 2 2 1 1':18.0, '3 1 1 3 2 2 2': 18.0, '3 3 2 2 2 1 1': 18.0, '2 1 2 2 1 3 3': 17.0, '1 2 2 2 3 3 1': 16.0}
# G = grey_wolf_algorithm(dict_of_parents_with_makespan)
# new_list = G.Mutation()
# # print(new_list)
