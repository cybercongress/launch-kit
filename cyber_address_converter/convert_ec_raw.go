package main

import (
	"fmt"
	"github.com/ethereum/go-ethereum/common"
	"github.com/cybercongress/cosmos-address-tool/crypto"
	"github.com/cybercongress/cosmos-address-tool/storage"
	"github.com/pkg/errors"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

const (
	addressFlag   = "address"
	accPrefixFlag = "acc-prefix"
)

// Usage: cosmos-address-tool convert-ethereum-cosmos --address=0x7C4401aE98F12eF6de39aE24cf9fc51f80EBa16B --acc-prefix=cyber
func CosmosAddressCmd() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "convert-ethereum-cosmos",
		Short: "Calculates for given ethereum address cosmos-based chain address with given prefix",
		RunE: func(cmd *cobra.Command, args []string) error {

			db, err := storage.OpenDb("eth-pubkeys")
			if err != nil {
				return err
			}

			ethAddrHex := viper.GetString(addressFlag)

			if !common.IsHexAddress(ethAddrHex) {
				return errors.New("ETH address provided in wrong format")
			}

			ethAddr := common.HexToAddress(ethAddrHex)
			ethRawPubkey := db.GetAddressPublicKey(ethAddr)

			if ethRawPubkey == nil {
				return errors.New("No public key found for provided address")
			}

			cosmosAddr := crypto.CosmosAddressFromEthKey(ethRawPubkey)
			fmt.Printf("[Eth: %s] [Cosmos: %s]", ethAddrHex, crypto.EncodeToHex(cosmosAddr, viper.GetString(accPrefixFlag)))
			return nil
		},
	}
	cmd.Flags().String(addressFlag, "", "hex encoded eth address")
	cmd.Flags().String(accPrefixFlag, "cosmos", "cosmos-based chain acc prefix")

	_ = viper.BindPFlag(addressFlag, cmd.Flags().Lookup(addressFlag))
	_ = viper.BindPFlag(accPrefixFlag, cmd.Flags().Lookup(accPrefixFlag))
	return cmd
}
