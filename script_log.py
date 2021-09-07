from collections import Counter
import operator

path_load = "/var/log/nginx/access.log"
path_save = "/opt/report.txt"
list_ips = []
with open(path_load, 'r') as f:         #abrir .log y crear una lista con las ips
    for line in f:
        data = line.strip().split(' ')
        list_ips.append(data[0]) 
    ip_dict_counter = Counter(list_ips) #counter hace un dict con las ips y el número de logs
    ip_dict_sorted = dict(sorted(ip_dict_counter.items(),
                 key=operator.itemgetter(1), reverse=True)) #ordena el dict según num logs
with open(path_save, 'w') as fout:       #crea el archivo report.txt y escribe el dict ordenado
    for ip in ip_dict_sorted.items():
        fout.write(f'{ip[0]}\t {ip[1]}\n')
