echo "start to collecting gifts files"

cp ../cosmos_gift_tool/data/cosmos.csv ./data/cosmos.csv
echo "cosmos gift loaded"

cp ../ethereum_gift_tool/data/ethereum.csv ./data/ethereum.csv
echo "ethereum gift loaded"

cp ../urbit-gift_tool/data/ethereum.csv ./data/ethereum.csv
echo "ethereum gift loaded"

cp ../lifetime_rewards_tool/data/notebook/validators.csv ./data/validators.csv
echo "validators rewards loaded"

echo "start to collecting distribution files"

cp ../params/network_genesis.json ./data/network_genesis.json
cp ../distribution/cyber_distribution.json ./data/cyber_distribution.json
cp ../distribution/manual_distribution.json ./data/manual_distribution.json

echo "distribution files collected"

echo "start to build cyber address tool"
cd ../cyber_address_converter
go build -o cyber
echo "address tool ready for use"

echo "converting cosmos addresses into cyber"
./cyber convert-cosmos-batch ../genesis_generator_tool/data/cosmos.csv ../genesis_generator_tool/data/cosmos.csv --acc-prefix=cyber
echo "done"

echo "converting ethereum urbit addresses into cyber"
./cyber convert-ethereum-batch ../genesis_generator_tool/data/ethereum.csv ./eth-pubkeys --acc-prefix=cyber
mv ./ethereum.csv ../genesis_generator_tool/data/urbit.csv
echo "done"

echo "converting ethereum addresses into cyber"
./cyber convert-ethereum-batch ../genesis_generator_tool/data/ethereum.csv ./eth-pubkeys --acc-prefix=cyber
mv ./ethereum.csv ../genesis_generator_tool/data/ethereum.csv
echo "done"

echo "converting validators addresses into cyber"
./cyber convert-cosmos-batch ../genesis_generator_tool/data/validators.csv ../genesis_generator_tool/data/validators.csv --acc-prefix=cyber
echo "done"

cd ../genesis_generator_tool

echo "files preparation done. Starting compile genesis.json"
python3 genesis_generator.py
echo "genesis compiled and saved at ./data/genesis.json"