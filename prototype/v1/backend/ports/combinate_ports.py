import json


all_ports = []
for file_json in range(145):
    if file_json != 0:

        with open(f"data/page_{file_json}.json", "r") as file:
            ports_in_file = json.load(file)

        for port in ports_in_file:
            all_ports.append(port)

print(all_ports)

print(len(all_ports))
with open("all_ports.json", "w") as file:
    json.dump(all_ports, file)

