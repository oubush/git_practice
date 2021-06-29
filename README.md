# my_cheat_sheets

Create docstring templates in numpydoc formatting style  
`pyment -w -o numpydoc module_name.py`

Check style  
`flake8 module_name.py`

Install pyment from GitHub  
`pip install git+https://github.com/dadadel/pyment.git`  

Create tmux session  
`tmux new-session -s NAME`

Attach to tmux session  
`tmux attach -t NAME`

Jupyter on server  
`jupyter-notebook --no-browser --port 8899`

Connect to server with Jupyter  
`ssh -L 8899:localhost:8899 user@server`

ssh using keys  
client: `user/.ssh` contains `id_rsa` (private) and `id_rsa.pub`(public keys)
server: `.ssh` contains `authorized_keys` (you should insert here your public key)
