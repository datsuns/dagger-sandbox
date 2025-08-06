package main

import (
	"context"
	"fmt"

	"dagger.io/dagger/dag"
)

func main() {
	if err := build(context.Background()); err != nil {
		fmt.Println(err)
	}
}

func build(ctx context.Context) error {
	fmt.Println("Building with Dagger")

	defer dag.Close()

	// get reference to the local project
	src := dag.Host().Directory(".")

	// create empty directory to put build outputs
	// outputs := dag.Directory()

	c := dag.Container().From("alpine:latest")
	log, err := c.WithMountedDirectory("/tmp/my", src).WithExec([]string{"ls", "-l", "/tmp/my"}).Stdout(ctx)
	fmt.Println(log)

	return err
}
