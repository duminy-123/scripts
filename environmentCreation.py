# 1.1 Initialize the Workspace

# Import core modules
from azureml import core
from azureml.core import Workspace
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.authentication import ServicePrincipalAuthentication

sp_password = "kmtF_eFc7bbSfE1f-0jP9_cOk447.R10SC"

sp_auth = ServicePrincipalAuthentication(
    tenant_id="f65a5101-8129-4c35-bcf4-20989ef1ae3f",
    service_principal_id="f09c754d-4528-49e7-9b7a-ec380cfb72e4",
    service_principal_password=sp_password)

# Initialize the workspace
ws = Workspace(workspace_name="wsWorkHours",
               subscription_id="4c2a4ba5-ab19-4b83-bd2f-61a1751a0b14",
               resource_group="rgWorkHours",
               auth=sp_auth)


# 1.2 Environment Set Up

# Creates an environment and adds Conda dependencies
environment = Environment("WorkHours-pipeline-env-new1")
# Use a docker container
environment.docker.enabled = True
conda_dep = CondaDependencies()
# Add Conda dependencies to myenv
environment.python.conda_dependencies = conda_dep
# Defines the packages the model and scripts need to function
conda_dep.add_conda_package("pip")
conda_dep.add_pip_package("argparse")
conda_dep.add_pip_package("scipy")
conda_dep.add_pip_package("joblib")
conda_dep.add_pip_package("numpy")
conda_dep.add_pip_package("pandas")
conda_dep.add_pip_package("sklearn")
conda_dep.add_pip_package("datetime")
conda_dep.add_pip_package("statsmodels")
conda_dep.add_pip_package("pyodbc")
conda_dep.add_pip_package("sqlalchemy")


# Register
environment.register(ws)