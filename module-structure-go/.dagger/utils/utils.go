// utils/utils.go
package utils

import (
	"context"

	"dagger/module-structure-go/internal/dagger"
)

func FetchName(ctx context.Context, client *dagger.Client) (string, error) {
	return client.Container().
		From("alpine:latest").
		WithExec([]string{"apk", "add", "curl", "jq"}).
		WithExec([]string{"sh", "-c", "curl https://randomuser.me/api/ | jq -r .results[0].name"}).
		Stdout(ctx)
}
