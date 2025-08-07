import dagger
from dagger import dag, function, object_type, ReturnType


@object_type
class Hello:
    @function
    async def ignore_error_on_with_exec(self, string_arg: str) -> dagger.Container:
        c = dag.container().from_("alpine:latest").with_exec(["exit", "1"], expect=ReturnType.ANY)
        c = c.with_exec(["sh", "-c", "echo hello >tmp.txt"])
        c.file("tmp.txt").export("log.txt")
        return await c

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
