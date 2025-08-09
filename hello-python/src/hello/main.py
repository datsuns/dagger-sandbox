import dagger
from dagger import dag, function, object_type, ReturnType


@object_type
class Hello:
    @function
    async def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        d = dag.container().from_("alpine:latest").with_exec(["echo", f"new {string_arg}"])
        ret1 = await d.exit_code()
        d = d.with_exec(["exit", "1"], expect=ReturnType.ANY)
        ret2 = await d.exit_code()
        d = d.with_exec(["echo", f"ret is {ret1},{ret2}"])
        if ret2 == 0:
            d = d.with_exec(["echo", f"ret is {ret2}"])
        else:
            d = d.with_exec(["echo", "failed"])

        await d.terminal()
        print(await d.stdout())
        return await d

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

    @function
    async def export_docker_image(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        d = dag.container().from_("alpine:latest").with_exec(["echo", f"new {string_arg}"])
        return d
