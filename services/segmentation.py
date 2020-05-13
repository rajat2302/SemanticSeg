from keras.models import *
from services.data import *
from setting import RESOURCE_ROOT


def segment():
    new_model = load_model(os.path.join(RESOURCE_ROOT,'saved_model_latest.hdf5'))
    testGene = testGenerator(RESOURCE_ROOT,1)
    new_model.load_weights(os.path.join(RESOURCE_ROOT,"unet_membrane.hdf5"))
    results = new_model.predict_generator(testGene,steps=1,verbose=1)
    predict_path = saveResult(RESOURCE_ROOT,results)
    return predict_path

