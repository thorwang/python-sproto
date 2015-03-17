from pysproto import sproto_create, sproto_type, sproto_encode, sproto_decode, sproto_pack, sproto_unpack

with open("person.pb", "r") as fh:
    content = fh.read()
sp = sproto_create(content)
st = sproto_type(sp, "Person");
result = sproto_encode(st, {
    "name": "John",
    "id":1001,
    "email":"john737@163.com",
    "phone":[
        {
            "type" : 1,
            "number": "10086",
        },
    ],
    })

print "result length:", len(result)
print ''.join(["%02x" %ord(x) for x in result])
print "-------------------------"
print sproto_decode(st, result)
print "========================="
pack_result = sproto_pack(result)
print len(pack_result)
print ''.join(["%02x" %ord(x) for x in pack_result])
print "-------------------------"
unpack_result = sproto_unpack(pack_result)
print ''.join(["%02x" %ord(x) for x in unpack_result])
