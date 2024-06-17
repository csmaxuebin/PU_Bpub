import Get_Params
import Get_Rappor
import numpy
import itertools
import random
import time
import os
import csv

from JunctionTree import independent_marginal2, independent_marginal, independent_marginal3
from Estimate_Joint_Distribution import true_joint_distribution, unfold_pro_list
from numpy import power


def get_clique(range_size, clique_size, sample_size):
    ini_list2 = list(itertools.combinations(range(range_size), clique_size))
    zzz = [list(eachtuple) for eachtuple in ini_list2]
    random.seed(15)
    zlist = random.sample(zzz, sample_size)
    return zlist


def l2_err(pro, true_pro):
    leng = len(pro)
    delta_pro = numpy.array(pro) - numpy.array(true_pro)
    return 1.0 * numpy.sqrt(numpy.sum(numpy.power(delta_pro, 2)) / (1.0))


def get_avd(pro, true_pro):
    leng = len(pro)
    delta_pro = numpy.array(pro) - numpy.array(true_pro)
    #     max_delta=max(numpy.abs(delta_pro))
    #     return max_delta
    abs_delta = numpy.abs(delta_pro)
    return numpy.sum(abs_delta) / 2.0


def cos(vector1, vector2):
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


def get_max(pro, true_pro):
    max1 = max(pro)
    max2 = max(true_pro)

    return abs(max1 - max2)


def get_var(pro, true_pro):
    return numpy.var(numpy.array(pro) - numpy.array(true_pro))


fai_C = 0.4  # from 0.2, 0.3, 0.4, 0.5
f = 0.5  # from 0.1, 0.2, 0.3, 0.4, 0.5  *********
bloombit = 32
hashbit = 16
dt = 0.01
readlimit = 60000
samplerate = 0.02
sparse_rate = 0.0
for file_id in [2]:

    # att_num1,node_num1,true_node_num1,rowlist1,multilist1=Get_Params.get_file_info(file_id,readlimit,1.0)
    if samplerate != 2:
        att_num2, node_num2, true_node_num2, rowlist2, multilist2 = Get_Params.get_file_info(file_id, readlimit,
                                                                                             samplerate)

        # att1_clique = get_clique(att_num2, 1, 20)
        att2_clique = get_clique(att_num2, 2,20)  # [[0,1],[0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15],[0,2],[2,4],[4,6],[6,8],[8,10],[10,12],[12,14],[2,5],[2,7],[7,10]]
        att3_clique = get_clique(att_num2, 3,20)  # [[0,1,2],[6,7,8],[9,10,11],[12,13,14],[3,5,7],[9,11,13],[2,13,15],[3,5,9],[4,5,15],[8,11,13],[9,10,15]]
        att4_clique = get_clique(att_num2, 4,20)  # [[0,1,2,3],[4,5,6,7],[8,9,10,11],[2,4,6,8],[8,10,12,14],[3,6,8,11],[4,6,7,9],[2,4,7,8],[5,8,9,11],[3,5,6,14]]
        att5_clique = get_clique(att_num2, 5, 20)

        if file_id == 4:
            bloombit = 32
            hashbit = 4
            samplerate = 0.1
            # cluster_list = [att2_clique]
            # cluster_list = [att2_clique, att5_clique]
            cluster_list = [att2_clique ,att3_clique,att4_clique,att5_clique  ]
        else:
            bloombit = 128
            hashbit = 4
            samplerate = 0.02
            # cluster_list = [att2_clique, att3_clique]
            cluster_list = [att2_clique,att3_clique]
            # cluster_list = [att3_clique]
        for f in [0.1]:

            print('file_id', file_id, 'samplerate:', samplerate, 'sparse_rate:', sparse_rate, 'f', f)

            att_num2, node_num2, true_node_num2, rowlist_sparse, multilist_sparse, bit_cand_list3, bit_list3, bitsum_list3 = Get_Rappor.Get_rid_sparse(
                file_id, readlimit, samplerate, bloombit, hashbit, f, sparse_rate)

            freqrow1, freqnum1, freqrate1, freqrow2, freqnum2, freqrate2, newlist = Get_Params.get_static_info(att_num2,
                                                                                                               node_num2,
                                                                                                               rowlist_sparse,
                                                                                                               multilist_sparse)

            if file_id != 5:
                for each_k in cluster_list:
                    lenk = len(each_k[0])
                    for eachclique in each_k:
                        true_list, true_pro = true_joint_distribution(multilist2, rowlist2, eachclique)
                        print('true:', true_pro)
                        write_list1 = [[f, samplerate, lenk, true_pro, bloombit, hashbit]]
                        print(write_list1)
                        os.chdir('C:\Users\\28708\\Desktop\\DisHD\\outp')
                        with open('file-' + str(file_id) + 'true_pro_marginal40.csv', 'a') as fid:
                            fid_csv = csv.writer(fid)
                            fid_csv.writerows(write_list1)
