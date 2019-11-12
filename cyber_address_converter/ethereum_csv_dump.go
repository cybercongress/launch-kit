package main

import (
	"encoding/csv"
	"github.com/cybercongress/cosmos-address-tool/storage"
	"github.com/spf13/cobra"
	"os"
)

// Usage: cosmos-address-tool ethereum-csv-dump <path>
// Usage: cosmos-address-tool ethereum-csv-dump eth-pubkeys.csv
func DumpEthereumToCSVCmd() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "ethereum-csv-dump <path>",
		Short: "Copy all loaded ethereum's public keys from db into selected file in CSV format",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {

			db, err := storage.OpenDb("eth-pubkeys")
			if err != nil {
				return err
			}

			resultFile, err := os.Create(args[0])
			if err != nil {
				return err
			}
			defer resultFile.Close()
			writer := csv.NewWriter(resultFile)
			writer.Comma = ','
			defer writer.Flush()

			for address, key := range db.GetAddressesPublicKeys() {
				_ = writer.Write([]string{address, key})
			}
			return nil
		},
	}
	return cmd
}
