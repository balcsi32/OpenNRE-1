import opennre
model = opennre.get_model('wiki80_cnn_softmax')
print(model.infer({'text':'A Wilton híd a Wye folyó egyik fő átkelője volt', 'h': {'pos': (3,12)}, 't': {'pos': (15,41)}}))
model = opennre.get_model('wiki80_bert_softmax')
print(model.infer({'text':'A Wilton híd a Wye folyó egyik fő átkelője volt', 'h': {'pos': (3,12)}, 't': {'pos': (15,41)}}))
model = opennre.get_model('wiki80_bertentity_softmax')
print(model.infer({'text':'A Wilton híd a Wye folyó egyik fő átkelője volt', 'h': {'pos': (3,12)}, 't': {'pos': (15,41)}}))
model = opennre.get_model('tacred_bert_softmax')
print(model.infer({'text':'A Wilton híd a Wye folyó egyik fő átkelője volt', 'h': {'pos': (3,12)}, 't': {'pos': (15,41)}}))
model = opennre.get_model('tacred_bertentity_softmax')
print(model.infer({'text':'A Wilton híd a Wye folyó egyik fő átkelője volt', 'h': {'pos': (3,12)}, 't': {'pos': (15,41)}}))

