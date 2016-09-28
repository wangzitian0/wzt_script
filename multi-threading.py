# coding:utf-8
import requests
import random
import time
import multiprocessing

pic_link = [
    '90000B30-E7C2-461A-BE14-B5E69470A44E',
    '90001B12-2312-4B39-80B6-457ED49D6DFD',
    '90001CB4-DCFF-4BC3-B3E3-7FCE365D8D82',
    '90001D89-015E-4FAC-8446-854479CC5280',
    '90002E63-8C0A-4752-B462-646E67539DF0',
    '900039fe-b26f-4512-9297-ebfc67576083.jpg',
    '900041EB-3A5F-45A9-835E-BB14B378C026',
    '90005135-2A66-4E63-AFF7-DE34EAB0A867',
    '900052c7-48db-4674-b972-276a9e2f71b9.jpg',
    '900053A5-12D1-4BAD-8A9B-348C4A6729AE',
    '900054d2-25f7-4eb1-84de-d9fe36ab71a2.jpg',
    'c00030ee-e9f3-4bc2-8e74-93bffc9e23bb.jpg',
    '90005705-92B5-4A28-8D22-738F3023B6A6',
    '900060E2-DE0D-4886-8829-BCB4500640B9',
    '90006314-C008-4B75-AC22-37A7D11FC990',
    '90006604-image-5038b093-19d9-4933-a02e-3e32e51e2523',
    '90006604-image-881190f0-4658-4810-84a4-15926abc069a',
    '90006604_d1670307-35e9-4d31-b1ff-5d15876f2362.jpg',
    '90007439-DD93-4B28-B357-349DC2B50C2A',
    '900074508',
    '90007648-5673-4bbc-a77f-748934fa1b0d.jpg',
    '900076D7-CDEC-4B2A-9BCA-B611A1793CEB',
    '90008264-image-7102a592-f729-4ef1-a073-ea8f910eeae9',
    '90008264-image-798b515d-93b9-4f89-850e-f099a824b2a7',
    '90008264-image-8b07f6e2-fac5-40a8-ab13-3c1dae8e9426',
    '90008264-image-ddb447a2-e25b-4b0b-9898-f7ac8a762d39',
    '90008281-image-009d30c8-3e8b-44f0-9fba-7d93e84c4859',
    '90008281-image-07aa8100-29b2-4cf7-9abc-d0ff6de23e20',
    '90008281-image-0a27a091-2737-49d7-862b-ba695c0752ab',
    '90008281-image-0cbd79ee-5673-426e-a0bc-0fdb00839d30',
    '90008281-image-0de57357-c274-4a77-a0a1-534f1ae9c866',
    '90008281-image-0e578093-f85f-40c7-ae6a-2830eafa7961',
    '90008281-image-0e73ba90-6a0f-4d16-a5fc-1193cf0a6e1d',
    '90008281-image-11677470-b103-43cd-b172-9b44d6cfa96e',
    '90008281-image-14af479f-6172-494a-935d-284febeced65',
    '90008281-image-1bfb13c3-d754-4f3a-9d53-877ae80c396b',
    '90008281-image-1eb22d88-2b0a-40a2-9975-aa4997cd7061',
    '90008281-image-1ee4abc9-3826-4414-8741-64fb3ca85d69',
    '90008281-image-1eed5750-f08c-467f-9260-d8c002da6d80',
    '90008281-image-2531fd67-6d47-408c-83ba-6095d5742856',
    '90008281-image-25507778-eac3-4a2f-89b6-f0b3c1546501',
    '90008281-image-2786c599-65a5-4c30-ae6a-17d68484af0c',
    '90008281-image-27c845b8-0522-49dc-a2a0-7f77da40ea00',
    '90008281-image-2f56780d-397b-475d-b4c8-29a8a9a09d38',
    '90008281-image-30e0f328-6602-4f8f-b224-d4459c68691e',
    '90008281-image-32c68d1a-e73f-41af-bced-f5b6384883e9',
    '90008281-image-357b9223-c4b8-4bc9-b778-3b27f73a4f3b',
    '90008281-image-376edf37-26e9-478c-ad0a-a31b8301c73d',
    '90008281-image-38d82781-574f-4d1f-b0dd-261e71ed94c2',
    '90008281-image-3af9b456-6b58-4c7c-b931-3dbd199285ff',
    'A0004956-4A7E-4CFA-A15C-AE2FCD60D9BA',
    'A0004A3E-1840-406D-9F49-D45243ECCD42',
    'A00052CC-456B-4097-9A24-2560F99EEC45',
    'A0006C7F-2116-4E73-A8BA-CBF6C8277D2A',
    'A0006D2C-3CC8-4D32-8476-DBBB2ECF74E8',
    'A000769B-3325-44B1-A31E-08C42327F0C7',
    'A00096D7-BDFC-4797-9DF2-7E1EE70C5EC9',
    'A000A8FE-C460-4620-B0AC-D57D051C79E9',
    'A000F49E-50BD-4C34-993F-310279949366',
    'A00101C1-7D72-45BC-91A3-CDB8E2659970',
    'A0011859-D652-4AC0-96C1-C001FB229A20',
    'A0013A73-D158-4A48-A96E-A9D9E2A00237',
    'A0014650-BE24-43C6-B6A2-70CB6D690CF0',
    'A00153D8-8E1A-4ED9-8BF1-B71706EF7B83',
    'A00157CA-CED4-4E36-8C16-7792186E577E',
    'A00165F5-11BF-4048-BFAA-13127766B99B',
    'A0017834-81E6-406F-88B7-06010E928370',
    'A0019103-AFDA-4846-BDC9-11CB84F2FD7D',
    'A0019DFC-C9CC-43CB-AC99-561659359F32',
    'A001B234-2004-47AC-849E-586AA6312767',
    'A001BBDE-E0EF-4C96-B2EC-C99A6AD93E73',
    'A001D203-5A30-44A0-8180-63F87146337F',
    'A001D5FA-49E0-4493-A034-09D2B4FAAFAB',
    'A001E82B-4636-45E8-80A5-A03A77A95401',
    'A0020AA8-9F13-4D8E-BF6E-C3FD55082880',
    'A00210D8-D4CF-4A0D-ABAB-8279D61D8B6A',
    'A00210F6-8B57-4767-A1C8-378256FC679A',
    'A0021A35-517C-446C-BEC4-B337E8D34219',
    'A00243D8-C28B-46F1-AD06-60397A9330EB',
    'A0024408-9FE2-42F6-B3B5-736281297324',
    'A00268FF-1460-43B0-8A97-F3AE4493CB15',
    'A002797A-ADFB-424E-A2A9-37C08E51BA9D',
    'A0027AE5-BADB-4F3D-8DAC-0F5F77F7F0BA',
    'A0027C6C-B25A-498C-BBA4-A6A865B73B56',
    'A0028933-3217-4BCB-B8E0-D57A496A9E0F',
    'A002D842-AB27-4F7F-B878-04249E8AB1E7',
    'A002F759-BBA3-4002-A5DD-82C6545B49BE',
    'A0030F01-00E8-48C7-9281-7714B629C253',
    'A00314DB-9560-4A8B-A287-7D5D945AF2E3',
    'A0031598-624D-474D-AA92-5C940CF71688',
    'A0032D7D-A760-46D7-873F-EA1D53E3FA1B',
    'A0033C20-82FF-4376-8CA0-2B945991FF16',
    'A0034577-044A-47F4-BEC8-4CF3923B0CE3',
    'A0036C49-6C2B-4F12-A44E-08AD0E9EC040',
    'A00370B3-B687-459F-8066-CA8C4A028DE1',
    'A0037BB7-1716-49F4-96E7-246D00C42313',
    'A0037F64-E07E-4446-A061-608A4321C66D',
    'A0039E82-9ABF-4A16-9B72-A85047BC0C96',
    'A003AE57-CC1F-4F48-8072-96EE3915E468',
    'A003C092-EBE2-4651-BEE9-0A74C1AE15C7',
]


vsum = [0, 0, 0]
vinfo = ["totol-page", "auto-orient", "not-orient", ]
lock = multiprocessing.Lock()

def vget(url, op, info):
    stime = time.time()
    res = requests.get(url)
    ttime = time.time()
    # print res.status_code
    lock.acquire()
    if res.status_code != 200:
        print info, "error"
    else:
        vsum[op] += (ttime - stime)
        vsum[0] += 1
        print vsum[0],info, (ttime - stime), "\t(s)"
    lock.release()


def vlink(x):
    for i in range(10):
        rd = str(random.randint(500 + i * 10, 510 + i * 10))
        url = "https://o01ueauum.qnssl.com/" + x + \
            "?imageMogr2/auto-orient/thumbnail/!" + rd + "/format/png"
        vget(url, 1, vinfo[1]+"\t" + x + " /:" + rd + "\t")
        url = "https://o01ueauum.qnssl.com/" + x + \
            "?imageMogr2/thumbnail/!" + rd + "/format/png"
        vget(url, 2, vinfo[2]+"\t" + x + " /:" + rd + "\t")





from Queue import Queue
from threading import Thread

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception, e:
                print e
            finally:
                self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

if __name__ == '__main__':
    from random import randrange
    from time import sleep


    pool = ThreadPool(200)

    for i, d in enumerate(pic_link):
        pool.add_task(vlink, d)

    pool.wait_completion()
    print vinfo[0],vsum[0],"\t",vinfo[1], "/", vinfo[2], ":", vsum[1], "/", vsum[2]
