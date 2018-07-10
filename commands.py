
import darknet as dn
net = dn.load_net("cfg/tiny-yolo.cfg", "tiny-yolo.weights", 0)
meta = dn.load_meta("cfg/coco.data")
r = dn.detect(net, meta, "data/dog.jpg")
print (r)