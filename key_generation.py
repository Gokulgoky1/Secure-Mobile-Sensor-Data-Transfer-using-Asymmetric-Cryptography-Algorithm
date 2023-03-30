from tinyec import registry
import hashlib,secrets, binascii
import pickle
import os

def key_gen_user(user):
    directory = user
    parent_dir = "Keys/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    curve = registry.get_curve('brainpoolP256r1')
    privKey = secrets.randbelow(curve.field.n)
    path1="Keys/"+user+"/private.txt"
    file_out = open(path1,"w")
    file_out.write(str(privKey))
    file_out.close()
    list1= {"private_key": path1}
    pubKey = privKey * curve.g

    ok = {
        'value': pubKey
    }
    path2="Keys/"+user+"/public.dictionary"
    file_out = open(path2, "wb")
    list1["public_key"] = path2
    pickle.dump(ok, file_out)
    file_out.close()
    return list1