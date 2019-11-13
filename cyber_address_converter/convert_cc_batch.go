package main

import (
	"bufio"
	"encoding/csv"
	"io"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"github.com/tendermint/tendermint/libs/bech32"
)

// Usage: cosmos-address-tool convert-cosmos-batch ./cosmos-hub.csv ./output.csv --acc-prefix=cyber
func ConvertCosmosToCosmosCmd() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "convert-cosmos-batch <path-to-cosmos-csv> --acc-prefix=<prefix>",
		Short: "Converts cosmos addresses to another cosmos addresses with given prefixes",
		Args:  cobra.ExactArgs(2),
		RunE: func(cmd *cobra.Command, args []string) error {

			accs, balances, err := readAccounts(args[0])
			if err != nil {
				return err
			}

			resultFile, err := os.Create(args[1])
			if err != nil {
				return err
			}
			defer resultFile.Close()
			writer := csv.NewWriter(resultFile)
			writer.Comma = ','
			defer writer.Flush()

			for i:= range accs {

				_, bz, err := bech32.DecodeAndConvert(accs[i])
				if err != nil {
					return err
				}

				addr, err := bech32.ConvertAndEncode(viper.GetString(accPrefixFlag), bz)
				if err != nil {
					return err
				}

				//fmt.Printf("[Cosmos Address: %s] [Converted Address: %s] [Balance: %s]", accs[i], addr, balances[i])
				//println()

				r := writer.Write([]string{addr, balances[i]})
				if r != nil {
					return r
				}
			}

			return nil
		},
	}
	cmd.Flags().String(accPrefixFlag, "cosmos", "cosmos-based chain acc prefix")

	_ = viper.BindPFlag(accPrefixFlag, cmd.Flags().Lookup(accPrefixFlag))

	return cmd
}

func readAccounts(path string) ([]string, []string, error) {
	accs := make([]string, 0)
	balances := make([]string, 0)
	file, err := os.Open(path)
	if err != nil {
		return accs, balances, err
	}

	reader := csv.NewReader(bufio.NewReader(file))
	reader.Comma = ','

	for {

		line, err := reader.Read()
		if err == io.EOF {
			break
		} else if err != nil {
			return accs, balances, err
		}

		if err != nil {
			return accs, balances, err
		}
		accs = append(accs, line[0])
		balances = append(balances, line[1])
	}

	return accs, balances, nil
}