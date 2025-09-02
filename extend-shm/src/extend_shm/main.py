from dagger import dag, function, object_type, DefaultPath
import dagger
from typing import Annotated


@object_type
class ExtendShm:
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

    @function
    async def extend(self, d: Annotated[
        dagger.Directory,
        DefaultPath("."),
    ]
    ) -> dagger.Container:
        size = 2_147_483_647
        return await (
            d.docker_build()
            .with_mounted_temp("/shm", size=size)  # ここで tmpfs を確保
            .with_exec(["bash", "-lc", "mkdir -p /shm && chmod 1777 /shm"])
            .with_exec(["bash", "-lc", "df -h /shm && ls -ld /shm"])
        )
