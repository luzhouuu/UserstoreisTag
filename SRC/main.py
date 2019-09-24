import fasttext
import pandas as pd

tags = ['Capability','Sub-Capability','Epic']
tag = tags[1]

print(tag)
def training_model(tag, e = 20):
    training_file = "../Files/training_" + tag + ".txt"

    model = fasttext.train_supervised(input=training_file, lr=0.5, epoch=e,
                                      wordNgrams=2, loss='ova')
    model.save_model("../Model/model_" + tag + ".bin")

def Tagid(tag):
    df_tag = pd.read_csv('../Files/' + tag + 'TagID.csv')
    return(df_tag.to_dict()[tag])

def predict(userstory, tag):
    model_file = '../Model/model_'+ tag + '.bin'

    classifier = fasttext.load_model(model_file)       # load model
    label = classifier.predict(userstory)
    label = int(label[0][0].replace('__label__', ''))
    dic = Tagid(tag)
    return(dic[label])

def get_tagId(taglabel, tag):
    tag_file = pd.read_csv('../Files/'+ tag + 'TagID.csv')
    return int(tag_file[tag_file[tag] == taglabel]['TagID'])

# import SRC.RequestGoTag as RequestGoTag
# a = RequestGoTag.requestGoTag('as a hr', 1)
# print(type(a))
# for t in a:
#     print(t)