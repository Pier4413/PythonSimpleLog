Remove-Item -Recurse -Force dist/
Remove-Item -Recurse -Force logger.egg-info
python setup.py sdist
python -m twine upload --verbose --repository-url https://hera.delmasweb.net dist/*