import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 15})
# plt.rc('axes', labelsize=15)
# plt.rc('legend', fontsize=15)
# plt.rc('figure', titlesize=15) 

def PlotAbundanceSep(datapaths, outpath, datapath_labels):
    '''plot the abundance of datasets seperately'''

    print('-----------------Now plotting abundance distributions of each dataset seperately.-----------------')

    for j, idatapath in enumerate(datapaths):
        n_class = len(os.listdir(idatapath)) # count the number of classes in dataset
        list_class = os.listdir(idatapath) # list of class names

        list_n_image_class = []
        # list of the numbers of images in each class
        for iclass in list_class:
            if os.path.exists(idatapath + '/%s/training_data/' % iclass):
                n_image_class = len(os.listdir(idatapath + '/%s/training_data/' % iclass))
            else:
                n_image_class = len(os.listdir(idatapath + '/%s/' % iclass))

            list_n_image_class.append(n_image_class)

        dict_class = dict(zip(list_class, list_n_image_class))
        sorted_dict_class = sorted(dict_class.items(), key=lambda x: x[1], reverse=True) # sorted dictionary {class name: number of images}
        
        # plot abundance
        ax = plt.subplot(1, 1, 1)
        plt.figure(figsize=(13, 7))
        plt.xlabel('Class', fontsize=20)
        plt.ylabel('Number of images per class', fontsize=20)
        plt.grid(alpha=0.5, axis='y', which='both')
        # ax.set_xlabel('Class')
        # ax.set_ylabel('Abundance')

        for i in range(len(sorted_dict_class)):
            plt.bar(sorted_dict_class[i][0], sorted_dict_class[i][1], log=True, color='royalblue')
            # plt.xticks(rotation=90)
            plt.xticks(rotation=45, rotation_mode='anchor', ha='right')

        plt.tight_layout()
        Path(outpath).mkdir(parents=True, exist_ok=True)
        plt.savefig(outpath + 'abundance_%s.png' % datapath_labels[j])
        plt.close()
        ax.clear()


def PlotAbundance_overall(datapaths, outpath, datapath_labels):
    '''plot the overall abundance of datasets'''

    print('-----------------Now plotting overall abundance distributions of each dataset.-----------------')

    list_class_all = ['aphanizomenon', 'asplanchna', 'asterionella', 'bosmina', 'ceratium',
                     'chaoborus', 'collotheca', 'conochilus', 'copepod_skins', 'cyclops', 'daphnia', 'daphnia_skins', 
                     'diaphanosoma', 'diatom_chain', 'dinobryon', 'dirt', 'eudiaptomus', 'filament', 
                     'fish', 'fragilaria', 'hydra', 'kellicottia', 'keratella_cochlearis', 'keratella_quadrata', 
                     'leptodora', 'maybe_cyano', 'nauplius', 'paradileptus', 'polyarthra', 'rotifers', 
                     'synchaeta', 'trichocerca', 'unknown', 'unknown_plankton', 'uroglena']
    
    df = pd.DataFrame(index=datapath_labels, columns=list_class_all)

    for j, idatapath in enumerate(datapaths):
        list_class = os.listdir(idatapath) # list of class names

        # list of the numbers of images in each class
        for iclass in list_class:
            if os.path.exists(idatapath + '/%s/training_data/' % iclass):
                n_image_class = len(os.listdir(idatapath + '/%s/training_data/' % iclass))
            else:
                n_image_class = len(os.listdir(idatapath + '/%s/' % iclass))

            df.loc[datapath_labels[j], iclass] = n_image_class

    df = df.div(df.sum(axis=1), axis=0)

    # plt.figure(figsize=(10, 7))
    # plt.xlabel('Abundance density')
    # plt.ylabel('Datasets')

    df.plot(figsize=(15, 10), kind='barh', stacked=True, legend=False, colormap='nipy_spectral', fontsize=17)
    plt.xlabel('Abundance density', fontsize=21)
    plt.ylabel('Datasets', fontsize=21)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)

    plt.tight_layout()
    Path(outpath).mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath + 'abundance_comparison.png')
    plt.close()



def PlotAbundance(datapaths, outpath, datapath_labels):
    '''plot the abundance of two datasets together'''

    print('-----------------Now plotting abundance distributions of each dataset together.-----------------')

    list_class_rep = ['aphanizomenon', 'asplanchna', 'asterionella', 'bosmina', 'ceratium',
                     'chaoborus', 'collotheca', 'conochilus', 'copepod_skins', 'cyclops', 'daphnia', 'daphnia_skins', 
                     'diaphanosoma', 'diatom_chain', 'dinobryon', 'dirt', 'eudiaptomus', 'filament', 
                     'fish', 'fragilaria', 'hydra', 'kellicottia', 'keratella_cochlearis', 'keratella_quadrata', 
                     'leptodora', 'maybe_cyano', 'nauplius', 'paradileptus', 'polyarthra', 'rotifers', 
                     'synchaeta', 'trichocerca', 'unknown', 'unknown_plankton', 'uroglena']
    
    # # find the repetitive classes in selected datasets
    # for idatapath in datapaths:
    #     list_class = os.listdir(idatapath)
    #     list_class_rep = list(set(list_class) & set(list_class_rep))
    #     list.sort(list_class_rep)
    # # print('Repetitive classes of two datasets: {}'.format(list_class_rep))

    list_n_image_class_combined = []
    for idatapath in datapaths:
        list_n_image_class = []
        # list of the numbers of images in each class
        for iclass in list_class_rep:
            if os.path.exists(idatapath + '/%s/training_data/' % iclass):
                n_image_class = len(os.listdir(idatapath + '/%s/training_data/' % iclass))
            elif os.path.exists(idatapath + '/%s/' % iclass):
                n_image_class = len(os.listdir(idatapath + '/%s/' % iclass))
            else:
                n_image_class = 0

            list_n_image_class.append(n_image_class)

        list_n_image_class_combined.append(list_n_image_class)

    total_image_1 = np.sum(list_n_image_class_combined[0])
    total_image_2 = np.sum(list_n_image_class_combined[1])
    df_abundance = pd.DataFrame({'class': list_class_rep, 'dataset_1': np.divide(list_n_image_class_combined[0], total_image_1), 'dataset_2': np.divide(list_n_image_class_combined[1], total_image_2)})
    # df_abundance = pd.DataFrame({'class': list_class_rep, 'dataset_1': list_n_image_class_combined[0], 'dataset_2': list_n_image_class_combined[1]})
    df_abundance['ratio'] = df_abundance['dataset_2'] / df_abundance['dataset_1']
    df_abundance_sorted = df_abundance.sort_values(by='dataset_1', ascending=False, ignore_index=True)

    fig = plt.figure(figsize=(13, 7))
    ax = plt.subplot(1, 1, 1)
    ax.set_xlabel('Class', fontsize=20)
    ax.set_ylabel('Relative abundance', fontsize=20)
    # ax.set_ylabel('Abundance')

    x = np.arange(0, len(list_class_rep) * 2, 2)
    width = 0.5
    x1 = x - width / 2
    x2 = x + width / 2

    y1 = df_abundance_sorted['dataset_1']
    y2 = df_abundance_sorted['dataset_2']

    abundance_distance = AbundanceDistance(y1, y2)

    Path(outpath).mkdir(parents=True, exist_ok=True)

    with open(outpath + 'Abundance_Distance_{}_{}.txt'.format(datapath_labels[0], datapath_labels[1]), 'a') as f:
        f.write(f'\n Global Distance: {abundance_distance}\n')

    plt.bar(x1, y1, width=0.5, label=datapath_labels[0])
    plt.bar(x2, y2, width=0.5, label=datapath_labels[1])
    # plt.bar(x1, y1, width=0.5, label=datapath_labels[0], log=True)
    # plt.bar(x2, y2, width=0.5, label=datapath_labels[1], log=True)
    plt.grid(alpha=0.5, axis='y', which='both')
    plt.xticks(x, df_abundance_sorted['class'], rotation=45, rotation_mode='anchor', ha='right')
    # plt.title('Distance between datasets: %.3f' % abundance_distance)
    plt.yscale('log')

    # ax_2 = ax.twinx()
    # ax_2.set_ylabel('Ratio of two datasets')
    # ax_2.plot(x, df_abundance_sorted['ratio'], label='ratio', color='green', marker='.')

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)
    plt.tight_layout()
    plt.savefig(outpath + 'abundance_relative_{}_{}.png'.format(datapath_labels[0], datapath_labels[1]))
    # plt.savefig(outpath + 'abundance.png')
    plt.close()
    ax.clear()



def AbundanceDistance(abundance_percentage_1, abundance_percentage_2):
    p1, p2 = abundance_percentage_1, abundance_percentage_2
    p1_normalized = p1 / np.linalg.norm(p1)
    p2_normalized = p2 / np.linalg.norm(p2)
    assert np.absolute(np.linalg.norm(p1_normalized)) - 1 < 10e-8
    assert np.absolute(np.linalg.norm(p2_normalized)) - 1 < 10e-8
    overlap = np.dot(p1_normalized, p2_normalized)
    abundance_distance = 1 - overlap

    return abundance_distance 