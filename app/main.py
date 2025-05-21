import asyncio
import sys

import asyncssh
from lib import get_config, get_remotes, get_workflows

async def main():
    remotes = get_remotes()
    for remote in remotes:
        workflows = get_workflows()
        async with asyncssh.connect(remote['host'], username=remote['user'], password=remote['password']) as conn:
            for workflow in workflows:
                print('Workflow:', workflow['name'])
                print('-' * len(workflow['name']))
                for step in workflow['steps']:
                    print(f'{step["name"]}:')
                    result = await conn.run(step['command'], check=True)
                    print("STDOUT:", result.stdout)
                    print("STDERR:", result.stderr)
                print('-' * len(workflow['name']))



if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main()) 
    except (OSError, asyncssh.Error) as e:
        print(f'Error: {e}')
        sys.exit('SSH connection failed: ' + str(e))