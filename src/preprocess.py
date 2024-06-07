import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


#Get the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "points_50.csv")


# Importing the dataset
dataset = pd.read_csv(file_path)

#Round the values of the dataset to 4 decimal places
dataset = dataset.round(4)

#Add a column to use as index from 0 to the length of the dataset
dataset['n_label'] = range(0, len(dataset))

#delete the column p_label
dataset = dataset.drop('p_label', axis=1)

#New dataset with only one layer    
dataset_layer1 = dataset[dataset['N_layer'] == 1]
dataset_layer2 = dataset[dataset['N_layer'] == 2]
dataset_layer3 = dataset[dataset['N_layer'] == 3]
dataset_layer4 = dataset[dataset['N_layer'] == 4]
dataset_layer5 = dataset[dataset['N_layer'] == 5]
dataset_layer6 = dataset[dataset['N_layer'] == 6]
dataset_layer7 = dataset[dataset['N_layer'] == 7]
dataset_layer8 = dataset[dataset['N_layer'] == 8]
dataset_layer9 = dataset[dataset['N_layer'] == 9]
dataset_layer10 = dataset[dataset['N_layer'] == 10]

#Gather in a list
dataset_layers = [dataset_layer2, dataset_layer3, dataset_layer4, dataset_layer5, dataset_layer6, dataset_layer7, dataset_layer8, dataset_layer9, dataset_layer10]

#empty dataframe
df = pd.DataFrame(columns=['Source', 'S_X', 'S_Y', 'S_Z', 's_phi', 's_eta', 's_q', 's_pt', 's_d0', 's_z0','Target', 'T_X', 'T_Y', 'T_Z','t_phi', 't_eta', 't_q', 't_pt', 't_d0', 't_z0', 'weight'])

#field of view
angle=20

#use itertuples
for i in dataset_layer1.itertuples():
    for j in dataset_layer2.itertuples():
        #filtrar lados
        if i.N_side==0:
            if i.N_side==j.N_side or i.N_side==j.N_side-1 or j.N_side==11:
                p1=np.array([i.x,i.y])
                p2=np.array([j.x,j.y])
                dp=np.dot(p2-p1,p1)
                theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                if theta*180/np.pi<10:
                #Add to the dataframe the source and target i.Label and j.Label
                #Use concat instead of append
                    df = pd.concat([df, pd.DataFrame({'Source': [i.n_label], 'S_X': [i.x], 'S_Y': [i.y], 'S_Z': [i.z], 's_phi': [i.phi], 's_eta': [i.eta], 's_q': [i.q], 's_pt': [i.pt], 's_d0': [i.d0], 's_z0': [i.z0], 'Target': [j.n_label], 'T_X': [j.x], 'T_Y': [j.y], 'T_Z': [j.z], 't_phi': [j.phi], 't_eta': [j.eta], 't_q': [j.q], 't_pt': [j.pt], 't_d0': [j.d0], 't_z0': [j.z0], 'weight':[1]})], ignore_index=True)

        elif i.N_side==11:
            if i.N_side==j.N_side or i.N_side==j.N_side+1 or j.N_side==0:
                p1=np.array([i.x,i.y])
                p2=np.array([j.x,j.y])
                dp=np.dot(p2-p1,p1)
                theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                if theta*180/np.pi<10:
                    #Add to the dataframe the source and target i.Label and j.Label
                    #Use concat instead of append
                    df = pd.concat([df, pd.DataFrame({'Source': [i.n_label], 'S_X': [i.x], 'S_Y': [i.y], 'S_Z': [i.z], 's_phi': [i.phi], 's_eta': [i.eta], 's_q': [i.q], 's_pt': [i.pt], 's_d0': [i.d0], 's_z0': [i.z0], 'Target': [j.n_label], 'T_X': [j.x], 'T_Y': [j.y], 'T_Z': [j.z], 't_phi': [j.phi], 't_eta': [j.eta], 't_q': [j.q], 't_pt': [j.pt], 't_d0': [j.d0], 't_z0': [j.z0], 'weight':[1]})], ignore_index=True)
        
        else:
            if i.N_side==j.N_side or i.N_side==j.N_side+1 or i.N_side==j.N_side-1:
                p1=np.array([i.x,i.y])
                p2=np.array([j.x,j.y])
                dp=np.dot(p2-p1,p1)
                theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                if theta*180/np.pi<10:
                    #Add to the dataframe the source and target i.Label and j.Label
                    #Use concat instead of append
                    df = pd.concat([df, pd.DataFrame({'Source': [i.n_label], 'S_X': [i.x], 'S_Y': [i.y], 'S_Z': [i.z], 's_phi': [i.phi], 's_eta': [i.eta], 's_q': [i.q], 's_pt': [i.pt], 's_d0': [i.d0], 's_z0': [i.z0], 'Target': [j.n_label], 'T_X': [j.x], 'T_Y': [j.y], 'T_Z': [j.z], 't_phi': [j.phi], 't_eta': [j.eta], 't_q': [j.q], 't_pt': [j.pt], 't_d0': [j.d0], 't_z0': [j.z0], 'weight':[1]})], ignore_index=True)


#Loop over the remaining layers
for i in range(0,len(dataset_layers)-1):
    for j in dataset_layers[i].itertuples():
        for k in dataset_layers[i+1].itertuples():
            #filtrar lados
            if j.N_side==0:
                if j.N_side==k.N_side or j.N_side==k.N_side-1 or k.N_side==11:
                    #filtrar z
                    if (j.z > 0 and k.z > 0) or (j.z < 0 and k.z < 0):
                        p1=np.array([j.x,j.y])
                        p2=np.array([k.x,k.y])
                        dp=np.dot(p2-p1,p1)
                        theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                        if theta*180/np.pi<angle:
                            if j.t_label==k.t_label:
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[1]})], ignore_index=True)
                            else:
                                #weight = ((np.abs(j.phi)- np.abs(k.phi))/np.abs(j.phi) + (np.abs(j.eta)- np.abs(k.eta))/np.abs(j.eta) + (np.abs(j.pt)- np.abs(k.pt))/np.abs(j.pt) + (np.abs(j.d0)- np.abs(k.d0))/np.abs(j.d0) + (np.abs(j.z0)- np.abs(k.z0))/np.abs(j.z0))/5
                                weight = 0.5
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[weight]})], ignore_index=True)

            elif j.N_side==11:
                if j.N_side==k.N_side or j.N_side==k.N_side+1 or k.N_side==0:
                    #filtrar z
                    if (j.z > 0 and k.z > 0) or (j.z < 0 and k.z < 0):
                        p1=np.array([j.x,j.y])
                        p2=np.array([k.x,k.y])
                        dp=np.dot(p2-p1,p1)
                        theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                        if theta*180/np.pi<angle:
                            if j.t_label==k.t_label:
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[1]})], ignore_index=True)
                            else:
                                #weight = ((np.abs(j.phi)- np.abs(k.phi))/np.abs(j.phi) + (np.abs(j.eta)- np.abs(k.eta))/np.abs(j.eta) + (np.abs(j.pt)- np.abs(k.pt))/np.abs(j.pt) + (np.abs(j.d0)- np.abs(k.d0))/np.abs(j.d0) + (np.abs(j.z0)- np.abs(k.z0))/np.abs(j.z0))/5
                                weight = weight = 0.5
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[weight]})], ignore_index=True)
        
            else:
                if j.N_side==k.N_side or j.N_side==k.N_side+1 or j.N_side==k.N_side-1:
                    #filtrar z
                    if (j.z > 0 and k.z > 0) or (j.z < 0 and k.z < 0):
                        p1=np.array([j.x,j.y])
                        p2=np.array([k.x,k.y])
                        dp=np.dot(p2-p1,p1)
                        theta=np.arccos(dp/(np.linalg.norm(p1)*np.linalg.norm(p2-p1)))
                        if theta*180/np.pi<angle:
                            if j.t_label==k.t_label:
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[1]})], ignore_index=True)
                            else:
                                #weight = ((np.abs(j.phi)- np.abs(k.phi))/np.abs(j.phi) + (np.abs(j.eta)- np.abs(k.eta))/np.abs(j.eta) + (np.abs(j.pt)- np.abs(k.pt))/np.abs(j.pt) + (np.abs(j.d0)- np.abs(k.d0))/np.abs(j.d0) + (np.abs(j.z0)- np.abs(k.z0))/np.abs(j.z0))/5
                                weight = weight = 0.5
                                df=pd.concat([df, pd.DataFrame({'Source': [j.n_label], 'S_X': [j.x], 'S_Y': [j.y], 'S_Z': [j.z], 's_phi': [j.phi], 's_eta': [j.eta], 's_q': [j.q], 's_pt': [j.pt], 's_d0': [j.d0], 's_z0': [j.z0], 'Target': [k.n_label], 'T_X': [k.x], 'T_Y': [k.y], 'T_Z': [k.z], 't_phi': [k.phi], 't_eta': [k.eta], 't_q': [k.q], 't_pt': [k.pt], 't_d0': [k.d0], 't_z0': [k.z0], 'weight':[weight]})], ignore_index=True)


#Save the dataframe to a csv file with script_dir
df.to_csv(os.path.join(script_dir, 'grap_50.csv'), index=False)




#Group by layer
#grouped = dataset.groupby('N_layer')

#Get only the first layer
#first_layer = grouped.get_group(2)

"""
#Plots
plt.scatter(dataset_layer1['x'], dataset_layer1['y'])
plt.scatter(dataset_layer2['x'], dataset_layer2['y'],color='red')
plt.scatter(dataset_layer6['x'], dataset_layer6['y'],color='green')
plt.show()
"""

"""
#Plot
fig, ax = plt.subplots()
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label='Layer %s' % key)
plt.show()
"""
