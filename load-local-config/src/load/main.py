from typing import Annotated
import dagger
import os
import yaml
from dagger import dag, function, object_type, DefaultPath, Doc


def build_default_yml_path():
    dagger_cmd_exec_path = os.path.join(os.path.dirname(__file__), '..', '..')
    return os.path.join(dagger_cmd_exec_path, 'config.yml')


@object_type
class Load:
    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    @function
    async def test(self, source: Annotated[
        dagger.File, DefaultPath('config.yml'), Doc("hello-dagger source directory")
    ],) -> dagger.Container:
        raw = await source.contents()
        print(raw)
        cfg = yaml.safe_load(raw)
        print(cfg)
        # cfg = self.load_config(build_default_yml_path())
        # print(cfg)
        return await (
            dag.container()
            .from_("alpine:latest")
        )

    @function
    def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    @function
    async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
        """Returns lines that match a pattern in the files of the provided Directory"""
        return await (
            dag.container()
            .from_("alpine:latest")
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_exec(["grep", "-R", pattern, "."])
            .stdout()
        )
