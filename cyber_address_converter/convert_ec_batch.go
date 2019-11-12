package main

import (
	"encoding/csv"
	"github.com/ethereum/go-ethereum/common"
	"github.com/cybercongress/cosmos-address-tool/crypto"
	"github.com/cybercongress/cosmos-address-tool/storage"
	//"github.com/pkg/errors"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"os"
)

// Usage: cosmos-address-tool convert-ethereum-batch ./ethereum_snapshot.csv eth-pubkeys --acc-prefix=cyber
func ConvertEthereumToCosmosCmd() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "convert-ethereum-batch <path-to-ethereum-csv> <path-to-pubkeys-db> --acc-prefix=<prefix>",
		Short: "Converts ethereum addresses to cosmos addresses with given prefix",
		Args:  cobra.ExactArgs(2),
		RunE: func(cmd *cobra.Command, args []string) error {

			db, err := storage.OpenDb(args[1])
			if err != nil {
				println("debub1")
				return err
				println("debub10")
			}

			accs, balances, err := readAccounts(args[0])
			if err != nil {
				println("debub2")
				return err
				println("debub20")
			}

			resultFile, err := os.Create("ethereum.csv")
			if err != nil {
				return err
			}

			defer resultFile.Close()
			writer := csv.NewWriter(resultFile)
			writer.Comma = ','
			defer writer.Flush()


			for i:= range accs {
				ethAddr := common.HexToAddress(accs[i])
				ethRawPubkey := db.GetAddressPublicKey(ethAddr)
				if ethRawPubkey == nil {
					println(accs[i])
					continue
				}
				cosmosAddr := crypto.CosmosAddressFromEthKey(ethRawPubkey)
				convertedAddr:= crypto.EncodeToHex(cosmosAddr, "cyber")

				//fmt.Printf("[Ethereum Address: %s] [Converted Address: %s] [Balance: %s]", accs[i], convertedAddr, balances[i])
				//println()

				err := writer.Write([]string{convertedAddr, balances[i]})
				if err != nil {
					return err
				}
			}

			return nil
		},
	}
	cmd.Flags().String(accPrefixFlag, "cosmos", "cosmos-based chain acc prefix")
	_ = viper.BindPFlag(accPrefixFlag, cmd.Flags().Lookup(accPrefixFlag))

	return cmd
}
