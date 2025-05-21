import asyncio
import sys
import argparse

import asyncssh
from lib import get_remotes, get_workflows

async def main(config_path=None):
    remotes = get_remotes(config_path)
    for remote in remotes:
        workflows = get_workflows(config_path)
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
    parser = argparse.ArgumentParser(description="Remote workflow runner")
    parser.add_argument('--config', type=str, default=None, help='Path to config YAML file')
    args = parser.parse_args()
    try:
        asyncio.get_event_loop().run_until_complete(main(args.config)) 
    except (OSError, asyncssh.Error) as e:
        print(f'Error: {e}')
        sys.exit('SSH connection failed: ' + str(e))