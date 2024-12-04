usersInfo = ['root:x:0:0:root:/root:/bin/ash' ,'bin:x:1:1:bin:/bin:/sbin/nologin' ,\
'daemon:x:2:2:daemon:/sbin:/sbin/nologin', \
'adm:x:3:4:adm:/var/adm:/sbin/nologin', \
'lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin', \
'sync:x:5:0:sync:/sbin:/bin/sync' ]


for items in usersInfo:
    items = items.split(':')
    User = items[0]
    print(f'USER: {User}')
    DEFAULT_SHELL = items[6]
    print(f'DEFAULT SHELL: {DEFAULT_SHELL}')
    HOME_DIRECTORY = items[5]
    print(f'HOME DIRECTORY: {HOME_DIRECTORY}')
    print()

