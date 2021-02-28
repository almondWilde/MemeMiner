#temux
#update pip and apt first
pkg install wget
$PREFIX/bin/wget https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh
apt install opencv

python -m pip install -r requirements.txt
