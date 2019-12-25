package main

import (
	"bufio"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"os"

	shell "github.com/ipfs/go-ipfs-api"
)

// Global variable to handle all the IPFS API client calls
var sh *shell.Shell

// Clone the repo and just run `go get && go run main.go`

func main() {

	// Where your local node is running on localhost:5001
	sh = shell.NewShell("localhost:5001")

	fmt.Println("###########################\n   Welcome to IPLD-CRUD!\n###########################\n")
	fmt.Println("This client generates a dynamic key-value entry and stores it in IPFS!\n")

	// Map structure to record key-value information
	m := make(map[string]interface{})

	accs, balances, _ := readAccounts("data.csv")

	for i := range accs {
		m[accs[i]] = balances[i]
	}

	// Converting into JSON object
	entryJSON, err := json.Marshal(m)
	if err != nil {
		fmt.Println(err)
	}

	// Display the marshaled JSON object before sending it to IPFS
	jsonStr := string(entryJSON)
	fmt.Println("The JSON object of your key-value entry is:")
	fmt.Println(jsonStr)

	// Dag PUT operation which will return the CID for futher access or pinning etc.
	cid, err := sh.DagPut(entryJSON, "json", "cbor")
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %s", err)
		os.Exit(1)
	}
	fmt.Println("------\nOUTPUT\n------")
	fmt.Printf("WRITE: Successfully added %sHere's the IPLD Explorer link: https://explore.ipld.io/#/explore/%s \n", string(cid+"\n"), string(cid+"\n"))

	fmt.Printf("READ: Value for key \"%s\" is: ", "key")
	res, err := GetDag(cid, accs[0])
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(res)
}

// GetDag handles READ operations of a DAG entry by CID, returning the corresponding value
func GetDag(ref, key string) (out interface{}, err error) {
	err = sh.DagGet(ref+"/"+key, &out)
	return
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
