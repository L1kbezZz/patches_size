import json
# import requests

def bytes_to_mb(size):
    result = size / 1024 / 1024

    return round(result, 2)

def get_update_size(version):
    client_content_tm = 0
    hdcontent = 0
    from_version = False
    from_scratch_cl = False
    from_scratch_hd = False
    patches = json.load(open('/root/test/patches.json'))
    for patch in patches:
        if patch['from_version'] != '0':
            if from_version == False:
                if patch['from_version'] == version:
                    from_version = True
                    if patch['part'] == 'client' or patch['part'] == 'content' or patch['part'] == 'tm':
                        for i in range(len(patch['patch_files'])):
                            client_content_tm += int(patch['patch_files'][i]['file_size'])
                            if from_scratch_cl == True:
                                client_content_tm_from_scratch += int(patch['patch_files'][i]['file_size'])
                    elif patch['part'] == 'hdconent':
                        for i in range(len(patch['patch_files'])):
                            hdcontent += int(patch['patch_files'][i]['file_size'])
                            if from_scratch_hd == True:
                                hdcontent_from_scratch += int(patch['patch_files'][i]['file_size'])
            else:
                if patch['part'] == 'client' or patch['part'] == 'content' or patch['part'] == 'tm':
                    for i in range(len(patch['patch_files'])):
                        client_content_tm += int(patch['patch_files'][i]['file_size'])
                        if from_scratch_cl == True:
                            client_content_tm_from_scratch += int(patch['patch_files'][i]['file_size'])
                elif patch['part'] == 'hdcontent':
                    for i in range(len(patch['patch_files'])):
                        hdcontent += int(patch['patch_files'][i]['file_size'])
                        if from_scratch_hd == True:
                            hdcontent_from_scratch += int(patch['patch_files'][i]['file_size'])

        elif patch['from_version'] == '0' and patch['part'] == 'hdcontent':
            if from_scratch_hd == False:
                hdcontent_from_scratch = 0
            from_scratch_hd = True
            id_hd = patch['id']
            for i in range(len(patch['patch_files'])):
                hdcontent_from_scratch += int(patch['patch_files'][i]['file_size'])

        elif patch['from_version'] == '0' and (patch['part'] == 'client' or patch['part'] == 'content' or patch['part'] == 'tm'):
            if from_scratch_cl == False:
                client_content_tm_from_scratch = 0
            from_scratch_cl = True
            id_cl = patch['id']
            for i in range(len(patch['patch_files'])):
                client_content_tm_from_scratch += int(patch['patch_files'][i]['file_size'])

        #print(from_version)
        #print(patch['id'])
        #print(patch['part'])
        #print(patch['from_version'])
        #print()

    print("Update from version: {}".format(version))
    print("Update Client Size = {}mb".format(bytes_to_mb(client_content_tm)))
    print("Update hdcontent size = {}mb".format(bytes_to_mb(hdcontent)))
    #print("SCRATCH_ID_CL = {}".format(id_cl))
    #print("SCRATCH_ID_HD = {}".format(id_hd))
    print("Install Client from scratch size = {}mb".format(bytes_to_mb(client_content_tm_from_scratch)))
    print("Install hdcontent from scratch size = {}mb".format(bytes_to_mb(hdcontent_from_scratch)))
    print("New commit")

#responce = requests.get('http://wgus-wotkis160.kdo.space/wgus/api/v4/patches', headers={'Authorization': 'Token vl5qGk3K7K641q8PfVteE3RTyyg97YFK'})
#print(responce)

get_update_size('2.0.3.358106')