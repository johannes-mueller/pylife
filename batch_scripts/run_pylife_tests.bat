call conda activate ./_venv

call python setup.py build_ext --inplace --force --define CYTHON_TRACE

call python -m pytest -v -ra --cache-clear -m ""  --junit-xml=junit.xml --cov-report xml:coverage_report.xml --cov-report html:coverage_report --cov=pylife || exit /B 1

call python batch_scripts\test_cov_analysis.py E:\pyLife_coverage\
