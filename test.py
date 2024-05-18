import os

print(os.environ['WORKFLOW_ENV'])
print(os.environ['ENV_FROM_JOB'])

print('env from environement github action')
print(os.environ['FROM_ENVIRONMENT_GITHUB_ACTION_2'])
print(os.environ['FROM_ENVIRONMENT_GITHUB_ACTION'])