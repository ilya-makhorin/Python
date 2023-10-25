# people = ['Yury', 'Prerpetuj', 'Masha']
# max_length = 0
# for person in people:
#     if len(person) <= max_length:
#         pass
#     else:
#         max_word = person
#         max_length = len(person)
#
# print('Самое длиное имя:', max_word)

#
# with open("data/RusDictionary.txt", encoding="utf-8") as f:
#     text = f.read()
# words = text.split("\n")
#
# with open("data/RusDictionary.txt", encoding="utf-8") as file:
#  words = file.read().split("\n")


# def is_reverse(word1, word2):
#   return word1[::-1] == word2
#
#
# with open("data/RusDictionary.txt", encoding="utf-8") as file:
#  words = [word.strip() for word in file.readlines()]
#
# for i in range(len(words)):
#  for j in range(i + 1, len(words)):
#   if is_reverse(words[i], words[j]):
#    print(f'{words[i]}-{words[j]}')

# for word in words:
#  reversed_word = word[::-1]
#  if reversed_word == word and word != '':
#   print(word, '-', reversed_word)


# def find_max_difference(filename):
#     with open(filename) as file:
#         pi_digits = file.read(1000)
#
#     max_difference = None
#     start = None
#     end = None
#     even_count = 0
#     odd_count = 0
#
#     for i, digit in enumerate(pi_digits):
#         if int(digit) % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#
#         difference = even_count - odd_count
#
#         if max_difference is None or difference > max_difference:
#             max_difference = difference
#             start = i - even_count + 1
#             end = i
#
#         if difference < 0:
#             even_count = 0
#             odd_count = 0
#
#     return {'start': start, 'end': end, 'difference': max_difference}
#
#
# result = find_max_difference('data/pi.txt')
# print(result)




import paramiko

ssh_hosts = [
    {"url": "yand.dyndns.org", "port": 1922, "user": "student"},
    {"url": "95.165.133.145", "port": 1922, "user": "student"},
]

password = "Pa$$w0rd"

for host in ssh_hosts:
    host_url = host["url"]
    host_port = host["port"]
    host_user = host["user"]

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host_url, port=host_port, username=host_user, password=password)

        # Проверяем наличие файла /etc/python3
        stdin, stdout, stderr = ssh_client.exec_command("ls /etc/python3")
        if "No such file or directory" in stderr.read().decode():
            print(f"Файл /etc/python3 не найден на хосте {host_url}")
        else:
            print(f"Файл /etc/python3 найден на хосте {host_url}")

        ssh_client.close()

    except paramiko.AuthenticationException:
        print(f"Ошибка аутентификации на хосте {host_url}")
    except paramiko.SSHException as e:
        print(f"Ошибка SSH-соединения с хостом {host_url}: {str(e)}")
    except Exception as e:
        print(f"Ошибка при выполнении команды на хосте {host_url}: {str(e)}")


# import os
#
# hosts = ['127.0.0.1', 'ya.ru', 'bad.bad', '8.8.8.8']
# for host in hosts:
#     command = f'ping -c 1 {host}'
#     # os.system(command)
#     result = os.popen(command).read()
#     if result.find('0.0% packet loss') < 0:
#         print(f'host {host} is bad')

