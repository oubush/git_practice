## conda commands (from DataCamp class)

Command | Description
--- | ---
conda list | list installed packages
conda env list | list conda environments
conda -h | help
conda list -n myenv | list of packages in myenv conda environment
conda install mypack=17.3.0 | install mypack package with version 17.3.0 (MAJOR.MINOR.PATCH)
conda install -c channel-name mypack | install mypack from channel-name
conda update mypack | update mypack
conda remove mypack | remove mypack
conda search mypack | search for compatible versions of mypack (--info - more information)
anaconda search mypack | search channels with mypack
conda --version | version of conda
conda list mypack | mypack information in current conda environment
conda list --name myenv mypack | mypack information in myenv conda environment
conda activate myenv | activate myenv
conda deactivate | deactivate current conda environment
conda env remove --name myenv | remove myenv
conda env export -n myenv | export myenv (usually in a file environment.yml by using >)
conda env create -n myenv --file filename | create myenv using filename

## more conda commands

Command | Description
--- | ---
