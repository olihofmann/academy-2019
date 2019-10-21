#%% Import
import io
import os

from collections import defaultdict
from surprise import KNNBasic
from surprise import Reader, Dataset
from surprise import get_dataset_dir

#%% Read Data Items
def read_movie_names():
    file_name = os.path.abspath("Recommender-System/ml-100k/u.item")
    rawid_to_name = {}
    name_to_rawid = {}
    
    with io.open(file_name, "r", encoding="ISO-8859-1") as f:
        for line in f:
            line = line.split('|')
            rawid_to_name[line[0]] = line[1]
            name_to_rawid[line[1]] = line[0]

    return rawid_to_name, name_to_rawid

#%% Top-N
def get_top_n(predictions, n=10):
    top_n = defaultdict(list)
    for uid, iid, _, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

#%% Load Data
file_path = os.path.abspath("Recommender-System/ml-100k/u.data")

reader = Reader(line_format="user item rating timestamp", sep="\t")
data = Dataset.load_from_file(file_path, reader=reader)
trainset = data.build_full_trainset()

#%% Build Similarity Matrix
sim_options = {"name": "pearson_baseline", "user_based": False}
algo = KNNBasic(sim_options=sim_options)
algo.fit(trainset)

#%% Read Movie Names
rawid_to_name, name_to_rawid = read_movie_names()

#%% Get inner id
toy_story_raw_id = name_to_rawid['Toy Story (1995)']
toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)

#%% Retrive neighbors
toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)

#%% Convert inner ids of the neighbors into names
toy_story_neighbors = (algo.trainset.to_raw_iid(inner_id)
                       for inner_id in toy_story_neighbors)

toy_story_neighbors = (rawid_to_name[rid]
                       for rid in toy_story_neighbors)

#%% Print Neighbors
print('The 10 nearest neighbors of Toy Story are:')
for movie in toy_story_neighbors:
    print(movie)

#%% Predict
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

#%% Get Top-N
top_n = get_top_n(predictions, n=10)

for uid, user_ratings in top_n.items():
    print(uid, [rawid_to_name[iid] for (iid, _) in user_ratings])

#%%
