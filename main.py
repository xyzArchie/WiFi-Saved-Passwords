import os

os.system('title [Saved WiFi Passwords]')
networks = [
    line.split(': ')[1] for line in os.popen('netsh wlan show profile').read().splitlines()
    if 'User Profile' in line
]

for network in networks:
    print(f'Network: {network}')
os.system(f'title [Saved WiFi Passwords] - Networks: {len(networks)}')

if 'Run as administrator' in os.popen('netsh wlan export profile folder=. key=clear').read():
    print('\nTo view all the passwords, relaunch the program as Administrator.')
else:
    os.system('cls && netsh wlan export profile folder=. key=clear >NUL')

    for file in os.listdir(os.curdir):
        if file.endswith('.xml'):
            network = file.replace('Wi-Fi-', '').replace('.xml', '')
            with open(file, 'r') as f:
                password = f.read().split('<keyMaterial>')[1].split(
                    '</keyMaterial>'
                )[0].replace('&lt;', '<').replace('&gt;', '>')
                print(f'Network: {network.ljust(30)}| Password: {password}')
                with open('WiFi Passwords.txt', 'a') as f:
                    f.write(f'Network: {network.ljust(30)}| Password: {password}\n')

    for file in os.listdir(os.curdir):
        if file.endswith('.xml'):
            os.remove(file)

os.system('pause >NUL')
