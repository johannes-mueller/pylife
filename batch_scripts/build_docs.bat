call conda activate ./_venv

call conda install sphinx=2.4.4
call conda install -c conda-forge m2r nbsphinx ipykernel make --yes
call pip install nbsphinx-link 
call pip install sphinx-rtd-theme

for /f "tokens=*" %%a in ('git rev-parse --show-toplevel') do (set repo_path=%%a)

set jupyter_path=%repo_path%_venv/Scripts/jupyter

call cd doc
call make html
call cd ..
