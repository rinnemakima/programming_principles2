import json

file_path = r'C:\Users\CoolUser\Desktop\pp2\programming_principles2\lab4\json1\sample-data.json'

with open(file_path) as json_file:
    data = json.load(json_file)

dns = []
descriptions = []
speeds = []
mtus = []

print("Interface status")
print("=" * 80)
print(f"{'DN':<45} {'Description':<15} {'Speed':<6} {'MTU':<6}")
print("-" * 45 + " " + "-" * 15 + " " + "-" * 6 + " " + "-" * 6)

for imdata in data["imdata"]:
    for key in imdata:
        for inner_key in imdata[key]:
            dn = imdata[key][inner_key]["dn"]
            description = imdata[key][inner_key].get("descr", "")
            speed = imdata[key][inner_key]["speed"]
            mtu = imdata[key][inner_key]["mtu"]
            
            print(f"{dn:<45} {description:<15} {speed:<6} {mtu:<6}")
            dns.append(dn)
            descriptions.append(description)
            speeds.append(speed)
            mtus.append(mtu)
