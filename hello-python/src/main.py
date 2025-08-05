import sys

import anyio
import dagger
from dagger import dag
from hello import Hello


async def main(args: list[str]):
    async with dagger.connection() as client:
        hello = Hello()
        container = await hello.container_echo("Hello from Dagger container_echo!")
        echo_result = await container.stdout()
        print(echo_result)

        source_dir = dag.host().directory("hello", exclude=["__pycache__"])
        grep_result = await hello.grep_dir(source_dir, "dagger")
        print(grep_result)

        # build container with cowsay entrypoint
        ctr = (
            dag.container()
            .from_("python:alpine")
            .with_mounted_directory("/mnt", source_dir)
            .with_exec(["ls", "/mnt"])
        )

        # run cowsay with requested message
        result = await ctr.stdout()
    print(result)


anyio.run(main, sys.argv[1:])
