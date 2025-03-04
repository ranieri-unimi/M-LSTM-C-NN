import numpy as np

aaa_path = r""

''' Load train set '''

X = None
y = None

var_list = []
for i in range(X.shape[0]):
    var_count = X[i].shape[-1]
    var_list.append(var_count)

var_list = np.array(var_list)
max_nb_timesteps = var_list.max()
min_nb_timesteps = var_list.min()
median_nb_timesteps = np.median(var_list)

print('max nb timesteps train : ', max_nb_timesteps)
print('min nb timesteps train : ', min_nb_timesteps)
print('median_nb_timesteps nb timesteps train : ', median_nb_timesteps)

X_train = np.zeros((X.shape[0], X[0].shape[0], max_nb_timesteps))
y_train = y[0]

# pad ending with zeros to get numpy arrays
for i in range(X_train.shape[0]):
    var_count = X[i].shape[-1]
    X_train[i, :, :var_count] = X[i]

''' Load test set '''
X = None
y = None


X_test = np.zeros((X.shape[0], X[0].shape[0], max_nb_timesteps))
y_test = y

# pad ending with zeros to get numpy arrays
for i in range(X_test.shape[0]):
    var_count = X[i].shape[-1]
    X_test[i, :, :var_count] = X[i]


''' Save the datasets '''
print("Train dataset : ", X_train.shape, y_train.shape)
print("Test dataset : ", X_test.shape, y_test.shape)
print("Train dataset metrics : ", X_train.mean(), X_train.std())
print("Test dataset : ", X_test.mean(), X_test.std())
print("Nb classes : ", len(np.unique(y_train)))

np.save(aaa_path + 'X_train.npy', X_train)
np.save(aaa_path + 'y_train.npy', y_train)
np.save(aaa_path + 'X_test.npy', X_test)
np.save(aaa_path + 'y_test.npy', y_test)