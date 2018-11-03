import napalm

device_ip = '10.10.10.26'
username = 'admin'
password = 'password123'

napalm_driver = napalm.get_network_driver('ios')
device = napalm_driver(hostname=device_ip,
                       username=username,
                       password=password)

device.open()

device.load_merge_candidate(filename='iou-r1-startup-config')
