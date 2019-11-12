package main

import (
	"github.com/cybercongress/cosmos-address-tool/storage"
	"github.com/spf13/cobra"
)

// Usage: cosmos-address-tool merge-ethereum-dbs from to
// Usage: cosmos-address-tool merge-ethereum-dbs collector-6350 eth-pubkeys
func MergeEthereumDbsCmd() *cobra.Command {

	cmd := &cobra.Command{
		Use:   "merge-ethereum-dbs",
		Short: "Copy all public keys from one db into other",
		Args:  cobra.ExactArgs(2),
		RunE: func(cmd *cobra.Command, args []string) error {

			fromDb, err := storage.OpenDb(args[0])
			if err != nil {
				return err
			}

			toDb, err := storage.OpenDb(args[1])
			if err != nil {
				return err
			}

			toDb.MergeDbs(&fromDb)
			return nil
		},
	}
	return cmd
}
