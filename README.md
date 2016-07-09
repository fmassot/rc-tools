# rc-tools

[![Build Status](https://travis-ci.org/fmassot/rc-tools.svg)](https://travis-ci.org/fmassot/rc-tools)

## Install :
```bash
pip install -r requirements.txt
```

## Launch tests :

```bash
python -m unittest discover
```

## Commands :

### NosDéputés.fr

 * Print and save in missing_urls.txt amendements which are not in nosdeputes database :

```python
python nosdeputes/manage.py check_if_amendement_are_in_db 2012-01-01 --end-date 2015-01-01
```

 * Make liasse of a given texteloi_id : 

```python
python nosdeputes/manage.py make_liasse 2173
```

### NosSénateurs.fr

 * Print and save in missing_urls.txt questions which are not in nossenateurs database :

```python
python nossenateurs/manage.py check_if_questions_are_in_db 2016-01-01
```