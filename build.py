import os
import subprocess
os.system("rm -rf packer-plugin-virtualbox*")
version = 'v2.0.6'
x = []
os.system(f'go build -o packer-plugin-virtualbox_{version}_x5.0_darwin_arm64 .')
os.system(
    f'zip packer-plugin-virtualbox_{version}_x5.0_darwin_arm64.zip packer-plugin-virtualbox_{version}_x5.0_darwin_arm64')
h1 = subprocess.getoutput(f'shasum -a 256 packer-plugin-virtualbox_{version}_x5.0_darwin_arm64.zip').split(' ')[0]
os.system(f'go build -o packer-plugin-virtualbox_{version}_x7.0_darwin_arm64 .')
# os.system(
#     f'zip packer-plugin-virtualbox_{version}_x7.0_darwin_arm64.zip packer-plugin-virtualbox_{version}_x7.0_darwin_arm64')
# h2 = subprocess.getoutput(f'shasum -a 256 packer-plugin-virtualbox_{version}_x7.0_darwin_arm64.zip').split(' ')[0]
x.append([h1, f'packer-plugin-virtualbox_{version}_x5.0_darwin_arm64.zip'])
# x.append([h2, f'packer-plugin-virtualbox_{version}_x7.0_darwin_arm64.zip'])
with open(f'packer-plugin-virtualbox_{version}_SHA256SUMS', 'w', encoding='utf8') as f:
    for item in x:
        f.write(f'{item[0]}  {item[1]}\n')

os.system('git add .')
os.system('git commit -s -m "over"')
os.system('git push liushuo')
os.system(f'git tag {version}')
os.system('git push liushuo --tags')
