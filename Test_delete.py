from statistics import median
import gzip, sys, os, re, io

path_directory = 'D:\\Павел\\Учеба\\МТУСИ\\5Семестр\\ИТиП\\Лабы\\Логи'
list_files = os.listdir(path_directory)
list_repeat_URl = []
count_list = len(list_files)
max_date = 0
def read_log(file):
    total_count = 0
    result = {}
    for line in file:
        regex = re.compile(r'\"[A-Z]+ ([^\s]+) .* (\d+\.\d+)\n')
        parsed_line = re.findall(regex, line)
        total_count += 1
        if parsed_line and parsed_line[0]:
            url = parsed_line[0][0]
            time = parsed_line[0][1]
            if url not in result:
                result[url] = []
                result[url].append(float(time))
            else:
                result[url].append(float(time))
    for key in result:
        print(
        f'key : {key}; '
        f'count = {len(result[key])}; '
        f'count_perc = {len(result[key]) / total_count}; '
        f'time_avg = {sum(result[key]) / len(result[key])}; '
        f'time_max = {max(result[key])}; '
        f'time_med = {median(result[key])}; '
        )

if count_list == 0:
    print("Логов нет")
    sys.exit()

for name in list_files:
    regex = re.compile(r"nginx-access-ui\.log-(\d{8})(\.gz)?")
    value = re.findall(regex, name)
    date = int(value[0][0])
    if max_date < date:
        max_date = date
        name_file = name
print(max_date)
print(name_file)


if name_file.lower().endswith('.gz'):
# if Path(name_file).suffix == '.gz':
    with gzip.open(path_directory + "\\" + name_file, "r") as file:
        with io.TextIOWrapper(file, encoding='utf-8') as file:
            read_log(file)
else:
    with open(path_directory + "\\" + name_file, 'r') as file:
        read_log(file)

