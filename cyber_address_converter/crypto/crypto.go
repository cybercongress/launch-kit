package crypto

import (
	"github.com/ethereum/go-ethereum/common"
	eth "github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"math/big"
)

var big8 = big.NewInt(8)

func GetPubKey(tx *eth.Transaction) (common.Address, []byte) {

	var signer eth.Signer = eth.FrontierSigner{}
	if tx.Protected() {
		signer = eth.NewEIP155Signer(tx.ChainId())
	}

	sighash := signer.Hash(tx)
	Vb, R, S := tx.RawSignatureValues()

	// EIP155 support
	var V byte
	if Vb.Int64() > 28 {
		v := new(big.Int).Sub(Vb, tx.ChainId())
		v = new(big.Int).Sub(v, tx.ChainId())
		v = new(big.Int).Sub(v, big8)
		V = byte(v.Uint64() - 27)
	} else {
		V = byte(Vb.Uint64() - 27)
	}

	r, s := R.Bytes(), S.Bytes()
	sig := make([]byte, 65)
	copy(sig[32-len(r):32], r)
	copy(sig[64-len(s):64], s)
	sig[64] = V

	// recover the public key from the signature
	var addr common.Address
	pubkey, _ := crypto.Ecrecover(sighash[:], sig)
	copy(addr[:], crypto.Keccak256(pubkey[1:])[12:])
	return addr, pubkey
}
