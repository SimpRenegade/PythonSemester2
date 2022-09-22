os.chdir('/home/user03/data')
currenttime = time.time()
for f in os.listdir('/home/user03/data/'):
    access_time = os.path.getatime(f)
    since_access = currenttime - access_time
    if since_access <= 86400:
        print(f)
