import json

data = json.load(open('/data2/yangxu/lxmert/data/vqa/nominival.json'))
N = len(data)
data_new = []
do_txt = open("gender.txt", "w")
play_txt = open("play.txt", "w")

for i in range(N):
    if data[i]['sent'].find('gender')>=0:
        data_new.append(data[i])
        print(data[i]['img_id'])
        print(data[i]['sent'])
        print(data[i]['label'])
        do_txt.write("{0}\n".format(data[i]['img_id']))
        do_txt.write("{0}\n".format(data[i]['sent']))
        do_txt.write("{0}\n".format(data[i]['label']))
    # if data[i]['sent'].find('gender')>=0:
    #     data_new.append(data[i])
    #     print(data[i]['img_id'])
    #     print(data[i]['sent'])
    #     print(data[i]['label'])
    #     play_txt.write("{0}\n".format(data[i]['img_id']))
    #     play_txt.write("{0}\n".format(data[i]['sent']))
    #     play_txt.write("{0}\n".format(data[i]['label']))

do_txt.close()
# play_txt.close()

# data = json.load(open('/data2/yangxu/lxmert/data/vqa/train.json'))
# N = len(data)
# c0 = 0
# w0 = 'surfboard'
# c1 = 0
# w1 = 'man'
# c2 = 0
# w2 = 'woman'
#
# for i in range(N):
#     if data[i]['sent'].find(w0)>=0:
#         c0 += 1
#         if data[i]['sent'].find(w1) >= 0:
#             c1 += 1
#         if data[i]['sent'].find(w2) >= 0:
#             c2 += 1
# print(w0,c0)
# print(w1,c1)
# print(w2,c2)