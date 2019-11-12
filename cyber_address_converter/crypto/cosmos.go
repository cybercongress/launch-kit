package crypto

import (
	"github.com/cosmos/cosmos-sdk/types"
	"github.com/tendermint/btcd/btcec"
	"github.com/tendermint/tendermint/crypto/secp256k1"
	"github.com/tendermint/tendermint/libs/bech32"
)

func CosmosAddressFromEthKey(ethRawPubkey []byte) types.AccAddress {

	var ethCompressedPubkey [33]byte
	ethPubkey, _ := btcec.ParsePubKey(ethRawPubkey[:], btcec.S256())
	copy(ethCompressedPubkey[:], ethPubkey.SerializeCompressed()[:])

	cbdPubKey := secp256k1.PubKeySecp256k1(ethCompressedPubkey)
	cbdAddr := types.AccAddress(cbdPubKey.Address())
	return cbdAddr
}

func EncodeToHex(address types.AccAddress, accPrefix string) string {
	bech32Addr, err := bech32.ConvertAndEncode(accPrefix, address.Bytes())
	if err != nil {
		panic(err)
	}
	return bech32Addr
}
