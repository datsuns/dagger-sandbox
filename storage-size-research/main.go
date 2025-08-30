// A generated module for StorageSize functions
//
// This module has been generated via dagger init and serves as a reference to
// basic module structure as you get started with Dagger.
//
// Two functions have been pre-created. You can modify, delete, or add to them,
// as needed. They demonstrate usage of arguments and return types using simple
// echo and grep commands. The functions can be called from the dagger CLI or
// from one of the SDKs.
//
// The first line in this comment block is a short description line and the
// rest is a long description with more detail on the module's purpose or usage,
// if appropriate. All modules should have a short description.

package main

import (
	"context"
	"dagger/storage-size/internal/dagger"
	"path/filepath"
)

type StorageSize struct{}

// Returns a container that echoes whatever string argument is provided
func (m *StorageSize) ContainerEcho(stringArg string) *dagger.Container {
	return dag.Container().From("alpine:latest").WithExec([]string{"echo", stringArg})
}

// Returns lines that match a pattern in the files of the provided Directory
func (m *StorageSize) GrepDir(ctx context.Context, directoryArg *dagger.Directory, pattern string) (string, error) {
	return dag.Container().
		From("alpine:latest").
		WithMountedDirectory("/mnt", directoryArg).
		WithWorkdir("/mnt").
		WithExec([]string{"grep", "-R", pattern, "."}).
		Stdout(ctx)
}

func (m *StorageSize) Hello(
	ctx context.Context,
	directoryArg *dagger.Directory,
	// +optional
	pattern string) (string, error) {
	if pattern == "" {
		pattern = "default"
	}
	return dag.Container().
		From("alpine:latest").
		WithWorkdir("/home").
		WithExec([]string{"sh", "-c", "echo default > file"}).
		WithExec([]string{"grep", "-R", pattern, "."}).
		Stdout(ctx)
}

func (m *StorageSize) None(
	ctx context.Context,
) (string, error) {
	return "hello", nil
}

func (m *StorageSize) Wget(
	ctx context.Context,
) *dagger.Container {
	return dag.Container().
		From("ubuntu").
		WithWorkdir("/tmp").
		WithExec([]string{"apt", "update"}).
		WithExec([]string{"apt", "install", "-y", "wget"}).
		WithExec([]string{"wget", "--no-check-certificate", "https://github.com/VOICEVOX/voicevox_core/raw/refs/heads/main/model/sample.vvm/decode.onnx"}).
		WithExec([]string{"wget", "--no-check-certificate", "https://github.com/VOICEVOX/voicevox_core/raw/refs/heads/main/model/sample.vvm/vocoder.onnx"})
}

func (m *StorageSize) Shell(
	ctx context.Context,
	dir *dagger.Directory,
) *dagger.Container {
	apt_cache := dag.CacheVolume("apt_cache")
	dl_cache := dag.CacheVolume("dl_cache")
	dl_cache_location := "/tmp/download"
	return dag.Container().
		From("ubuntu:22.04").
		WithMountedCache("/var/lib/apt/lists", apt_cache).
		WithMountedCache("/var/cache/apt", apt_cache).
		WithMountedCache(dl_cache_location, dl_cache).
		WithMountedDirectory("/work", dir).
		WithWorkdir("/work").
		WithExec([]string{"apt", "update"}).
		WithExec([]string{"apt", "install", "-y", "wget"}).
		WithExec([]string{"bash", "-x", "dl.sh", dl_cache_location})
}

func (m *StorageSize) MountHuge(
	ctx context.Context,
	dir *dagger.Directory,
) *dagger.Container {
	apt_cache := dag.CacheVolume("apt_cache")
	dl_cache := dag.CacheVolume("dl_cache")
	local_cache := dag.CacheVolume("local_cache")
	dl_cache_location := "/tmp/download"
	local_cache_location := "/work"
	work_location := "/work"
	return dag.Container().
		From("ubuntu:22.04").
		WithMountedCache("/var/lib/apt/lists", apt_cache).
		WithMountedCache("/var/cache/apt", apt_cache).
		WithMountedCache(dl_cache_location, dl_cache).
		WithMountedCache(local_cache_location, local_cache).
		WithMountedDirectory(work_location, dir).
		WithWorkdir(work_location).
		WithExec([]string{"apt", "update"}).
		WithExec([]string{"apt", "install", "-y", "wget", "make", "gcc", "git", "libncurses-dev"}).
		WithExec([]string{"git", "clone", "-b", "test", "https://github.com/datsuns/vim.git"}).
		WithWorkdir(filepath.Join(work_location, "vim")).
		WithExec([]string{"./configure"}).
		WithExec([]string{"make", "-j", "8"}).
		WithExec([]string{"make", "install"})
}
