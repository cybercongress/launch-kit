package main

import (
	"context"
	"fmt"
	"github.com/spf13/cobra"
	"os"
)

var ctx = context.Background()

func main() {

	var rootCmd = &cobra.Command{
		Use:   "cosmos-address-tool",
		Short: "Cosmos addresses transformer",
		Long: `Allows you to cast cosmos addresses, also support cast from Ethereum.`,
	}

	rootCmd.AddCommand(CollectCmd())
	rootCmd.AddCommand(CosmosAddressCmd())
	rootCmd.AddCommand(MergeEthereumDbsCmd())
	rootCmd.AddCommand(DumpEthereumToCSVCmd())
	rootCmd.AddCommand(ConvertEthereumToCosmosCmd())
	rootCmd.AddCommand(ConvertCosmosToCosmosCmd())

	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
